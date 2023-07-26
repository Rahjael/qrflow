from datetime import date
import os
import PySimpleGUI as sg

from generate_qrcode import generate_qr_code
from img2pdf_paster import paste_image_to_pdf
from pdf_to_image import pdf_to_image





def main():
    # Variables needed during program execution
    devmode = True
    today_date = date.today().strftime("%Y-%m-%d")
    is_valid_form = False
    temp_qr_filename = 'temp_qr.png'
    temp_pdf_filename = 'temp_pdf.png'
    select_pdf_filename = 'assets/select_pdf_file.png'
    fill_form_qr_filename = 'assets/fill_form_qr_file.png'
    output_images_path = 'output_images_path'
    pdf_preview_max_width = 250
    qr_preview_max_width = 250
    last_pdf_previewed = None
    temp_files_to_cleanup = [temp_pdf_filename, temp_qr_filename]
    qr_offset_x = 20
    qr_offset_y = 20
    qr_final_width = 100
    qr_final_height = 100


    # Define the layout of the GUI
    column_left = sg.Column([
        [sg.Frame("File:", [[sg.Input(autodetect_file(), key="-FILE-", expand_x=True), sg.FilesBrowse("Sfoglia", key="-BROWSE_FILES-", target="-FILE-", enable_events=True)]], expand_x=True)],
        [sg.Frame("Tipo documento:", [[sg.Listbox([
                                        "Ddt",
                                        "Fattura", 
                                        "Preventivo",
                                        "Verbale",
                                        "Altro"
                                        ], key="-DOC-", no_scrollbar=True, size=(50, 5), enable_events=True, expand_x=True)]], expand_x=True)],
        [sg.Frame("Numero documento:", [[sg.Input(key="-NUM-", enable_events=True, expand_x=True)]], expand_x=True)],
        [sg.Frame("Data documento:", [[sg.Input(today_date, key="-DATE-", enable_events=True, expand_x=True), sg.CalendarButton("Cambia data", format="%Y-%m-%d", key="-CALENDAR_BUTTON-", target="-DATE-", enable_events=True)]], expand_x=True)],
        [sg.Frame("Codice lavoro:", [[sg.Input(key="-CODE-", enable_events=True, expand_x=True)]], expand_x=True)],
        # [sg.one_line_progress_meter("Completamento...", 0, 3)],
        [sg.Text("Riempire correttamente tutti i campi per generare il qr.", key="-ALERT_FILL_FORM-", text_color="red")],
        [sg.Button("Applica QRCode", key="-APPLY_BUTTON-", disabled=False), sg.Checkbox("Sovrascrivi", key="-OVERWRITE_CHECKBOX-")]
    ],
    vertical_alignment="top")

    column_right = sg.Column([
        [sg.Image(select_pdf_filename, key="-PDF_THUMBNAIL-")],
        [sg.Image(fill_form_qr_filename, key="-QR_THUMBNAIL-")]
    ])

    layout = [
        [column_left, column_right]
    ]

    window = sg.Window("Apply QRCode to PDF", layout, finalize=False)




    # Event loop
    while True:
        event, values = window.read() # ! This is a blocking function. It goes on only when a PySimpleGUI event is triggered

        print(f"event: {event}, values: {values}") if devmode else None

        if event == sg.WIN_CLOSED or event == None:
            cleanup_temp_files(temp_files_to_cleanup)
            break
        
        # Update pdf preview
        if values["-FILE-"] != last_pdf_previewed and os.path.isfile(values["-FILE-"]):
            pdf_to_image(values["-FILE-"], output_images_path, temp_pdf_filename, 'png', pdf_preview_max_width)
            window["-PDF_THUMBNAIL-"].update(source=temp_pdf_filename)
            last_pdf_previewed = values["-FILE-"]



        # Detect if form is correctly filled
        # * I think it's better to try and update the qrcode at every event instead of checking for data to be complete
        # * This is because I want the user to be free to generate the code no matter the info at their disposal
        # if len(values["-CODE-"]) == 8 and values["-DATE-"] and values["-NUM-"] and (values["-DOC-"][0] if len(values["-DOC-"]) > 0 else False):

        # Delete current qrcode if present
        cleanup_temp_files([temp_qr_filename])

        data = {
            "DOC": values["-DOC-"][0] if len(values["-DOC-"]) > 0 else "",
            "NUM": values["-NUM-"],
            "DATE":values["-DATE-"],
            "CODE": values["-CODE-"] if len(values["-CODE-"]) == 8 else "", # TODO allow for more codes
            "OTHER": ""
            }
                 
        # The qr code is updated at every event
        generate_qr_code(data, temp_qr_filename, qr_preview_max_width, qr_preview_max_width)
        window["-QR_THUMBNAIL-"].update(source=temp_qr_filename)




        if event == "-APPLY_BUTTON-":
            print('Applying qrcode to pdf...')
            output_path = values["-FILE-"] # TODO implement functionality of overwrite checkbox
            paste_image_to_pdf(values["-FILE-"], temp_qr_filename, output_path, qr_offset_x, qr_offset_y, qr_final_width, qr_final_height)
            print('Done.')

            # Update pdf preview
            pdf_to_image(values["-FILE-"], output_images_path, temp_pdf_filename, 'png', pdf_preview_max_width)
            window["-PDF_THUMBNAIL-"].update(source=temp_pdf_filename)
            last_pdf_previewed = values["-FILE-"]


        # ! The form is currently NOT checked. Empty fields are allowed
        # window["-APPLY_BUTTON-"].update(disabled=True if is_valid_form == False else False)
        # window["-ALERT_FILL_FORM-"].update(visible=True if is_valid_form == False else False)

        window.refresh()

        # print(f'apply_button: {apply_button.Disabled}')



    # Close the window when the loop exits
    window.close()


def cleanup_temp_files(temp_files):
    # Clear temp files when program exits
    for path in temp_files:
        if os.path.exists(path):
            os.remove(path)
            print(f"The file '{path}' has been successfully deleted.")
        else:
            # print(f"The file '{path}' does not exist. Nothing to do.")
            pass


def autodetect_file():
    file_name = "Nessun file trovato"
    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        if filename.lower().endswith(".pdf"):
            file_name = os.path.abspath(filename)
            break

    return file_name



if __name__ == "__main__":
    main()

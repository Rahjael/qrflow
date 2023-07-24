from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io



def paste_image_to_pdf(pdf_path, image_path, output_path, x_pos, y_pos, width, height):
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()

    # Open the image
    image = Image.open(image_path)

    image.thumbnail((width, height))

    # Get image size in points (1 inch = 72 points)
    img_width, img_height = image.size
    img_width_pt = img_width * 0.75
    img_height_pt = img_height * 0.75



    # Adjust y-coordinate to position the top-left corner at (x_pos, y_pos)
    # y_pos = A4[1] - y_pos - img_height_pt

    # Iterate through the PDF pages
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        packet = io.BytesIO()

        # Create a new canvas and draw the image on it
        can = canvas.Canvas(packet, pagesize=A4)
        can.drawImage(image_path, x_pos, y_pos, width=img_width_pt, height=img_height_pt)
        can.save()

        # Move the buffer position to the start
        packet.seek(0)

        # Merge the image from the buffer with the current PDF page
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])

        # Add the modified page to the PDF writer
        pdf_writer.add_page(page)

    # Write the new PDF to the output file
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)





if __name__ == "__main__":
    pdf_path = "test_file.pdf"
    image_path = "test_image.png"
    output_path = "test_output.pdf"
    x_position = 20  # Replace with the desired X position in points
    y_position = 20  # Replace with the desired Y position in points
    width = 50
    height = 50

    paste_image_to_pdf(pdf_path, image_path, output_path, x_position, y_position, width, height)





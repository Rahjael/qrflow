import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:"), sg.Input(key="-NAME_INPUT-")],
    [sg.Text("Select your favorite color:"), sg.Listbox(["Red", "Green", "Blue"], size=(15, 3), key="-COLOR_LISTBOX-")],
    [sg.Text("Pick a date:"), sg.Input("YYYY-MM-DD", key="-CALENDAR_INPUT-"), sg.CalendarButton("Calendario", format="%Y-%m-%d", key="-CALENDAR_BUTTON-", target="-CALENDAR_INPUT-")],
    [sg.Button("Submit"), sg.Button("Exit")]
]

window = sg.Window("My Window", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    print(f"Event: {event}, Values: {values}")

window.close()
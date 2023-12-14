import PySimpleGUI as sg

sg.theme("DarkAmber")  # Add a touch of color
print(sg.theme_list())

#open windows

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("Demo", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
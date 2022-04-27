import PySimpleGUI as sg

layout =  [
  [sg.Text("Just simple text")],
  [sg.Button("OK")]
]

window = sg.Window("Demo", layout, margins=(250,200))
#sg.Window(title="Hello World", layout, margins=(250,200)).read()
while True:
  event, values = window.read()
  if event == "OK" or event == sg.WIN_CLOSED:
    break
window.close()

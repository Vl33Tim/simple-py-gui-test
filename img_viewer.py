#img_viewer.py
#from curses import window
from fileinput import filename
import os.path

import PySimpleGUI as sg

#window layout
file_list_column = [
  [
  sg.Text("image folder"),
  sg.In(size=(25,1),enable_events=True,key="-FOLDER-"),
  sg.FolderBrowse(),
  ],
  [
      sg.Listbox(
        values=[],size=(40,20),enable_events=True,key="-FILE LIST-"
      )
  ],
]
image_view_column = [

  [sg.Text("Choose an image from the list on the left:")],
  [sg.Text(size=(40,1), key=("-TOUT-"))],
  [sg.Image(key="-IMAGE-")]
]

#full layout
layout =[ 
  [
    sg.Column(file_list_column),
    sg.VSeparator(),
    sg.Column(image_view_column),
  ]
]

window = sg.Window("Image Viewer", layout)

#event loop

while True:
  event, values = window.read()
  if event == "Exit" or event == sg.WIN_CLOSED:
    break
  #folder name was filled in so make list of files
  if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    try:
      #get list of files in folder
      file_list = os.listdir(folder)
    except:
      file_list = []
    
    fnames = [
      f
      for f in file_list
      if os.path.isfile(os.path.join(folder, f))
      and f.lower().endswith((".png", ".gif"))
    ]
    window["-FILE LIST-"].update(fnames)
  elif event == "-FILE LIST-":
    try:
      filename = os.path.join(
        values["-FOLDER-"], values["-FILE LIST-"][0]
      )
      window["-TOUT-"].update(filename)
      window["-IMAGE-"].update(filename=filename)
    except:
      pass
      #window.close()


window.close()
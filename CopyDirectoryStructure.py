import os
from pathlib import Path
import PySimpleGUI as sg

def copy_directories(src, target):
    # src or target format: "/dir1/dir2/src_dir"
    
    folder_basename = os.path.basename(src)
    result_base_folder = os.path.join(target + "/", os.path.basename(src))
    os.makedirs(result_base_folder, exist_ok=True)
    print(result_base_folder)

    for (root,_,_) in os.walk(src):

        if (root == src): continue

        new_sub_dir = os.path.join(result_base_folder, root[len(src)+1:])
        print(new_sub_dir)
        os.makedirs(new_sub_dir, exist_ok=True)

select_dir_layout = [
    [
        sg.Text("Source Directory"),
        sg.In(size=(50, 1), enable_events=True, key="-src_folder-"),
        sg.FolderBrowse(),
        sg.Button("List Sub Directories", key="-src_list_dir_btn-"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(95, 20), key="-src_file_list-"
        )
    ],
]

target_dir_layout = [
    [
        sg.Text("Target Directory"),
        sg.In(size=(50, 1), enable_events=True, key="-target_folder-"),
        sg.FolderBrowse(),
        sg.Button("List target Sub Directories", key="-target_list_dir_btn-"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(95, 20), key="-target_file_list-"
        )
    ],
]

start_btn_layout = [
    [sg.Button("Start")],
    [sg.Text("Message box", key="-message-")],
]

layout = [
    [
        sg.Column(select_dir_layout),
        sg.VSeperator(),
        sg.Column(target_dir_layout),
    ],
    [sg.HSeparator()],
    [
        sg.Column(start_btn_layout),
    ]
]

window = sg.Window(title="Copy Directory Structure", layout = layout, margins=(100,50))

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == "-src_folder-":
        continue
        
    if event == "-src_list_dir_btn-":
        src_path = values["-src_folder-"]
        file_list = os.walk(src_path) if (os.path.isdir(src_path)) else []
        fnames = [
            (root)
            for (root, dirs, file) in 
            file_list
        ]
        window["-src_file_list-"].update(fnames)
        
    if event == "-target_folder-":
        continue
        
    if event == "-target_list_dir_btn-":
        target_path = values["-target_folder-"]
        file_list = os.walk(target_path) if (os.path.isdir(target_path)) else []
        fnames = [
            (root)
            for (root, dirs, file) in 
            file_list
        ]
        window["-target_file_list-"].update(fnames)
        
    if event == "Start":
        
        window["-src_folder-"].update(values["-src_folder-"].rstrip('/'))
        window["-target_folder-"].update(values["-target_folder-"].rstrip('/'))
        
        if values["-src_folder-"] == "": 
            window["-message-"].update("Source path is empty")
            continue
            
        if not os.path.exists(values["-src_folder-"]): 
            window["-message-"].update("Source path doesn't exist")
            continue
            
        if not os.path.isdir(values["-src_folder-"]): 
            window["-message-"].update("Source path is not a directory")
            continue

        if values["-target_folder-"] == "": 
            window["-message-"].update("Target path is empty")
            continue
            
        if not os.path.exists(values["-target_folder-"]): 
            window["-message-"].update("Target path doesn't exist")
            continue
            
        if not os.path.isdir(values["-target_folder-"]): 
            window["-message-"].update("Target path is not a directory")
            continue
        
        copy_directories(values["-src_folder-"], values["-target_folder-"])
        
        result_path = os.path.join(values["-target_folder-"] + "/", os.path.basename(values["-src_folder-"]))
        
        window["-target_folder-"].update(result_path)
        
        file_list = os.walk(result_path) if (os.path.isdir(result_path)) else []
        fnames = [
            (root)
            for (root, dirs, file) in 
            file_list
        ]
        
        window["-target_file_list-"].update(fnames)
        window["-message-"].update("Success")
        
            
window.close()

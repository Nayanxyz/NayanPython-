import FreeSimpleGUI as g
from zip_creator import make_archive

label1 = g.Text("Select the files to compress:")
input1 = g.Input()
button1 = g.FilesBrowse("Choose", key="files")           #choose feature has a key names files that will store value
                                                          #filesbrowse to select files
label2 = g.Text("Select the location to Save:")
input2 = g.Input()
button2 = g.FolderBrowse("Choose", key="folder")     #folderbrowse to select folders

compress_button = g.Button("Compress")
message_button = g.Text(key="output", text_color="Black")

window = g.Window("File Compressor to Zip", layout=[[label1, input1 , button1],[label2, input2 , button2],
                                                    [compress_button, message_button]])

while True:
    event, values = window.read()
    if event == g.WIN_CLOSED:              #event variable is whatever i click it becomes event
        break
    if event == "Compress":
        filepaths = values["files"].split(";")    #values variable store files key and split is used to split multiple files
        folders = values["folder"]                #make archive function has filepaths and folders variable  which replaces filepaths variable
                                                # in zip_creator.py filepaths and folder replaces dest_dir
        make_archive(filepaths , folders)
        window["output"].update(value="Compression completed")    #value means print here

window.close()
import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")  #Radio allows the user to choose exactly one option from a predefined set
option2 = sg.Radio("Fish", group_id="question1")        #small circle like options
option3 = sg.Radio("Mammals", group_id="question1")     #group_id is an optional parameter when creating a Radio element
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label], [option1],[option2],[option3], [option4]])

window.read()
window.close()
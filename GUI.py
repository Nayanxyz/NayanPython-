import FunctionComb

import FreeSimpleGUI as FSG                                 # FSG is short

label = FSG.Text("Type in a TO-DO")                 #Text is type in FSG
input_box = FSG.InputText(tooltip="Enter todo")     #tooltip is a tool to hoverr over box and InputText is also a Type
add_button =FSG.Button("Add")                       #Button is also a type for buttons

window = FSG.Window('My To-Do App', layout=[[label],[input_box, add_button]])      #Window is a type of FSG / layoout is a tool
window.read()
window.close()                                 #read method not to read but to display on window methods like title()

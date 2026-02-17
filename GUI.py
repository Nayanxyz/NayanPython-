import FunctionComb

import FreeSimpleGUI as FSG                                                      # FSG is short

import time

import os

if os.path.exists("dist/todos.txt"):
    with open("dist/todos.txt", "w") as file:
        pass

FSG.theme("GreenMono")

clock = FSG.Text("",key='clock')
label = FSG.Text("Type in a TO-DO")                                              #Text is type in FSG
input_box = FSG.InputText(tooltip="Enter todo", key="todo")                      #tooltip is a tool to hover over box and InputText is also a Type
add_button =FSG.Button("Add",size=10)                                                  #image_source for image implement ,mouseover_colors to click add button
                                                                                  #image size is image size
                                                                              #Button is also a type for buttons
list_box = FSG.Listbox(values=FunctionComb.todos_f(), key="todos",
                       enable_events=True , size=[45,10])
replace_button = FSG.Button("Replace")
remove_button = FSG.Button("Remove")
exit_button = FSG.Button("Exit", size=7)
window = FSG.Window('My To-Do App',  layout=[[clock],[label],[input_box, add_button],
                            [list_box, replace_button, remove_button],
                            [exit_button]],font=['Helvetica',20])
                                                                                 #Window is a type of FSG / layout is a tool
                                                                                 #[] list shows rows ..if add_button were to be in separate
                                                                                 # list then it would be on another row
while True:
    event, values = window.read(timeout=200)                                     #read method not to read but to display on window methods like title()
    if event != FSG.WIN_CLOSED:                                                  #clock is running even after i closed the window , so used if
        window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(1,event) #printing values in terminal helps us understand values and keys , very important thing i guess
    #print(2,values)
    #print(3, values['todos'])
    match event:
        case "Add":
            todos = FunctionComb.todos_f()
            new_todo = values['todo'] + '\n'                                  # values variable has todo key ,that has input value which i type
                                                                              # and all that inside new_todo variable
            todos.append(new_todo)                                           #update method to update current list in real time in todos file
            FunctionComb.todos_w(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")                             #update input_box with empty " "
        case "Replace":
            try:
                todo_to_replace = values['todos'][0]
                new_todo = values['todo']                                   #remember key to put values in[]

                todos = FunctionComb.todos_f()
                variable = todos.index(todo_to_replace)                     #storing every event in separate variables
                todos[variable]= new_todo
                FunctionComb.todos_w(todos)
                window['todos'].update(values=todos)                        #[todos] is key and values=todos is todos list
            except IndexError:
                FSG.popup("Please select a To-Do", font=['Helvetica',20])
        case "Remove":
            try:
                todo_to_remove = values['todos'][0]
                todos = FunctionComb.todos_f()
                todos.remove(todo_to_remove)                               # remove method
                FunctionComb.todos_w(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                FSG.popup("Please select to Remove",font=['Helvetica',20])

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])      #when user clicked a line in list , it shows in input box ,

        case FSG.WIN_CLOSED:
            break

window.close()

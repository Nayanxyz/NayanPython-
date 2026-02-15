import FunctionComb

import FreeSimpleGUI as FSG                                                      # FSG is short

label = FSG.Text("Type in a TO-DO")                                              #Text is type in FSG
input_box = FSG.InputText(tooltip="Enter todo", key="todo")                      #tooltip is a tool to hover over box and InputText is also a Type
add_button =FSG.Button("Add")                                                    #Button is also a type for buttons
list_box = FSG.Listbox(values=FunctionComb.todos_f(), key="todos",
                       enable_events=True , size=[45,10])
replace_button = FSG.Button("Replace")
window = FSG.Window('My To-Do App', layout=[[label],[input_box, add_button],[list_box, replace_button]],
                    font=['Helvetica',20])
                                                                                 #Window is a type of FSG / layout is a tool
                                                                                 #[] list shows rows ..if add_button were to be in separate
                                                                                 # list then it would be on another row
while True:
    event, values = window.read()                                                #read method not to read but to display on window methods like title()
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            todos = FunctionComb.todos_f()
            new_todo = values['todo'] + '\n'                                  # values variable has todo key ,that has input value which i type
                                                                              # and all that inside new_todo variable
            todos.append(new_todo)                                           #update method to update current list in real time in todos file
            FunctionComb.todos_w(todos)
            window['todos'].update(values=todos)
        case "Replace":
            todo_to_replace = values['todos'][0]
            new_todo = values['todo']

            todos = FunctionComb.todos_f()
            index = todos.index(todo_to_replace)
            todos[index]= new_todo
            FunctionComb.todos_w(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case FSG.WIN_CLOSED:
            break

window.close()

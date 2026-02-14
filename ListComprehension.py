while True :

    user = input("Add , Show , Replace , Remove or Exit : ")
    user = user.strip()

    match user:

        case "add" | "Add":
            todo = input("Add names :") +"\n"

            file = open('todos.txt', 'r')            #txt file todos and readlines/writelines method
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file_new = open('todos.txt', 'w')       #overwrites previous file to save previous contents of todos.txt file
            file_new.writelines(todos)
            file_new.close()

        case "show" | "Show":
            file = open('todos.txt','r')            #to open and read file only
            todos = file.readlines()                #defined todos
            file.close()

                                                       #new_todos = []

                                                       #for item in todos:
                                                          #new_item =item.strip('\n')
                                                          #new_todos.append(new_item)

            new_todos = [item.strip('\n') for item in todos]       #list comprehension , above code in one line

            for symb, item in enumerate(new_todos):


                row = f"{symb+1}-{item} "
                print(row)

        case "replace" | "Replace":
            number = int(input("type the number :"))
            number = number - 1
            new_todo = input("enter the word :")
            todos[number] = new_todo

        case "remove" | "Remove":
            number = int(input("type the number on the list word :"))
            todos.pop(number -1)

        case "exit" | "Exit":
            break

        case whatever:
            print("type add or show or exit")

print("Thanks !!")



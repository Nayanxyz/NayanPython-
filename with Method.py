while True :

    user = input("Add , Show , Replace , Remove or Exit : ")
    user = user.strip()

    match user:

        case "add" | "Add":
            todo = input("Add names :") +"\n"

            with open('todos.txt', 'r') as file:         #with is used to automatically close file and make code clean and short
                todos = file.readlines()                 #file = open('todos.txt','r')
                                                         #todos= file.readline()
            todos.append(todo)                           #file.close()

            with open('todos.txt', 'w') as file_new:
                file_new.writelines(todos)

        case "show" | "Show":

            with open('todos.txt','r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]       #list comprehension , above code in one line

            for symb, item in enumerate(new_todos):

                row = f"{symb+1}-{item} "
                print(row)

        case "replace" | "Replace":
            number = int(input("type the number :"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter the word :")

            todos[number] = new_todo +'\n'

            with open('todos.txt', 'w') as file:
                file.writelines()

        case "remove" | "Remove":
            number = int(input("type the number on the list word :"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            variable = number-1
            removing = todos[variable].strip('\n')

            todos.pop(variable)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"{removing} is removed from list"
            print(message)

        case "exit" | "Exit":
            break

        case whatever:
            print("type add or show or exit")

print("Thanks !!")



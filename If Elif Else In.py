while True :

    user = input("add , show , replace , remove or exit : ")
    user = user.strip()



    if "add" in user or 'Add' in user:               # If elif else conditional block and in ,or ,and, not operator
        todo = user[4:]                         #[4:] is list slicing , 4 is no. of chars of add_ and then value ..
                                                     #... afterwards it prints the given value
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo +'\n')

        with open('todos.txt', 'w') as file_new:
            file_new.writelines(todos)

    elif "show" in user:

        with open('todos.txt','r') as file:
            todos = file.readlines()

        for symb, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{symb+1}-{item}"
            print(row)

    elif "replace" in user:
        number = int(user[7:])

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = input("enter the word :")

        todos[number] = new_todos +'\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "remove" in user:
        number = int(user[6:])

        with open('todos.txt') as file:          #'r' as reading is defualt in open function
            todos = file.readlines()

        variable = number - 1
        removing = todos[variable].strip('\n')

        todos.pop(variable)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"{removing} is removed from list"
        print(message)

    elif "exit" in user:
        break

    else :
        print("command not valid")



print("Thanks !!")



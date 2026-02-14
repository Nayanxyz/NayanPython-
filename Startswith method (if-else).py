while True :

    user = input("add , show , replace , remove or exit : ")
    user = user.strip()



    if user.startswith('add'):               # If elif else conditional block and in ,or ,and, not operator
        todo = user[4:]                         #[4:] is list slicing , 4 is no. of chars of add_ and then value ..
                                                     #... afterwards it prints the given value
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo +'\n')

        with open('todos.txt', 'w') as file_new:
            file_new.writelines(todos)

    elif user.startswith('show'):
        with open('todos.txt','r') as file:
            todos = file.readlines()

        for symb, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{symb+1}-{item}"
            print(row)

    elif user.startswith('replace'):
        number = int(user[8:])

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = input("enter the word :")

        todos[number] = new_todos +'\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user.startswith('remove'):
        number = int(user[7:])

        with open('todos.txt') as file:          #'r' as reading is defualt in open function
            todos = file.readlines()

        variable = number - 1
        removing = todos[variable].strip('\n')

        todos.pop(variable)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"{removing} is removed from list"
        print(message)

    elif user.startswith('exit'):
        break

    else :
        print("command not valid")



print("Thanks !!")



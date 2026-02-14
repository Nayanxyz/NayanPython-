def todos_f(filenames="todos.txt"):                                  #custom function,, return is backbone
    with open(filenames, 'r') as files:                 #filenames = todos.txt default  or to make it default all the way
        todos_file = files.readlines()                  # we use filenames=todos.txt
        return todos_file

def todos_w(todos_arg,filenames='todos.txt'):                  #filenames=todos.txt//todos_arg=todos
    with open(filenames, 'w') as file_new:                     #(filenames='todos.txt',todos_arg) argument was like this but to make it default
        file_new.writelines(todos_arg)                         # we change position of todos_arg cause its a string and filenames is list

while True:

    user = input("add , show , replace , remove or exit : ")
    user = user.strip()

    if user.startswith('add'):                              # If elif else conditional block and in ,or ,and, not operator
        todo = user[4:]                                     # [4:] is list slicing , 4 is no. of chars of add_ and then value ..
                                                             # ... afterwards it prints the given value
        todos = todos_f()                               #filenames=todos.txt we can write like this too or just 'todos.txt'

        todos.append(todo + '\n')

        todos_w(todos)

    elif user.startswith('show'):

        todos = todos_f()

        for symb, item in enumerate(todos):

            item = item.strip('\n')

            row = f"{symb + 1}-{item}"

            print(row)

    elif user.startswith('replace'):
        try:                                             # try except used for error handling after except type Error name

            number = int(user[8:])

            number = number - 1

            todos = todos_f()

            new_todos = input("enter the word :")

            todos[number] = new_todos + '\n'

            todos_w(todos)

        except ValueError:
            print("Invalid command ")
            continue                                               # continue is apposite of break and starts with first inpu i.e user

    elif user.startswith('remove'):
        try:
            number = int(user[7:])

            todos = todos_f()                                      # 'r' as reading is defualt in open function


            variable = number - 1
            removing = todos[variable].strip('\n')

            todos.pop(variable)

            todos_w(todos)
            message = f"{removing} is removed from list"
            print(message)

        except (IndexError,ValueError):                        #handle two errors at same time
            print("invalid number , type show ")

    elif user.startswith('exit'):
        break

    else:
        print("command not valid")

print("Thanks !!")



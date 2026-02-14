#from FunctionComb import todos_f, todos_w   2 methods same work
import FunctionComb                                   #local module
import time

now = time.strftime("%b %d, %Y %H:%M:%S")             #strftime is standard module in python index module
print("It is", now)


while True:

    user = input("add , show , replace , remove or exit : ")
    user = user.strip()

    if user.startswith('add'):                              # If elif else conditional block and in ,or ,and, not operator
        todo = user[4:]                                     # [4:] is list slicing , 4 is no. of chars of add_ and then value ..
                                                             # ... afterwards it prints the given value
        todos = FunctionComb.todos_f()                               #filenames=todos.txt we can write like this too or just 'todos.txt'

        todos.append(todo + '\n')

        FunctionComb.todos_w(todos)

    elif user.startswith('show'):

        todos = FunctionComb.todos_f()

        for symb, item in enumerate(todos):

            item = item.strip('\n')

            row = f"{symb + 1}-{item}"

            print(row)

    elif user.startswith('replace'):
        try:                                             # try except used for error handling after except type Error name

            number = int(user[8:])

            number = number - 1

            todos = FunctionComb.todos_f()

            new_todos = input("enter the word :")

            todos[number] = new_todos + '\n'

            FunctionComb.todos_w(todos)

        except ValueError:
            print("Invalid command ")
            continue                                               # continue is apposite of break and starts with first inpu i.e user

    elif user.startswith('remove'):
        try:
            number = int(user[7:])

            todos = FunctionComb.todos_f()                                      # 'r' as reading is defualt in open function


            variable = number - 1
            removing = todos[variable].strip('\n')

            todos.pop(variable)

            FunctionComb.todos_w(todos)
            message = f"{removing} is removed from list"
            print(message)

        except (IndexError,ValueError):                        #handle two errors at same time
            print("invalid number , type show ")

    elif user.startswith('exit'):
        break

    else:
        print("command not valid")

print("Thanks !!")



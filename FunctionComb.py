#FILEPATH = "todos.txt"                       #this method helps us change data only on first variable
#def todos_f(filenames=FILEPATH)

def todos_f(filenames="todos.txt"):                                  #custom function,, return is backbone
    with open(filenames, 'r') as files:                 #filenames = todos.txt default  or to make it default all the way
        todos_file = files.readlines()                  # we use filenames=todos.txt
        return todos_file

def todos_w(todos_arg,filenames='todos.txt'):                  #filenames=todos.txt//todos_arg=todos
    with open(filenames, 'w') as file_new:                     #(filenames='todos.txt',todos_arg) argument was like this but to make it default
        file_new.writelines(todos_arg)                         # we change position of todos_arg cause its a string and filenames is list

print("hello there!")               #we can print anything on main code
                                   #what if you want this pregram to run and main program to not show print .
                                   #we have if conditional block
if __name__ == "__main__":
    print("hello hello")            #hello hello will not print in the main code but will print here
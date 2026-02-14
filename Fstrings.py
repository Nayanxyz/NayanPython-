todos = []          #USE dir(list) for exploring list functions and use { help(list.function) } to know its usage

while True :

    user = input("Add , Show , Replace , Remove or Exit : ")
    user = user.strip()                    #strip function does equal spaces throughout the code

    match user:

        case "add" | "Add":                           # | syntax is used for 'or'
            todo = input("Add names :")
            todos.append(todo)

        case "show" | "Show":
            for symb, item in enumerate(todos):       #symb is variable for number ,enumerate(functn)used to add numbers,
                                                      #and symbol before strings. {symb = symbol & item = strings}.
                row = f"{symb+1}-{item} "             #f string(functn)is used for adding symbols and  words thoughout list
                print(row)                            #+1 for list start from 1

        case "replace" | "Replace":
            number = int(input("type the number :"))
            number = number - 1
            new_todo = input("enter the word :")
            todos[number] = new_todo                  #todos is the list and [number] is the index
                                                      #indexing system replaces other input from the list that is new_todo replaces
        case "remove" | "Remove":
            number = int(input("type the number on the list word :"))
            todos.pop(number -1)                      #pop is used for remove obj when only type obj's number

        case "exit" | "Exit":
            break

        case whatever:                                #we can add variable after case.
            print("type add or show or exit")

print("Thanks !!")



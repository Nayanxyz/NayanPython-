todos = []

while True :

    user = input("Add , Show , Edit or Exit : ")
    user = user.strip()                    #strip function does equal spaces throughout the code

    match user:
        case "add" | "Add":                # | syntax is used for 'or'
            todo = input("Add names :")
            todos.append(todo)
        case "show" | "Show":
            for item in todos:             # item is a variable after for.loop and we can play with it
                item = item.upper()
                print(item)
        case "edit" | "Edit":
            number = int(input("type the number :"))
            number = number - 1
            new_todo = input("enter the word :")
            todos[number] = new_todo      #todos is the list and [number] is the index
        case "exit" | "Exit":             #indexing system replaces other input from the list that is new_todo replaces
            break
        case whatever:                    #we can add variable after case.
            print("type add or show or exit")
print("Thanks !!")



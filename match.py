todos = []

while True :

    user = input("Add , Show or Exit : ")
    user = user.strip()             #strip function does equal spaces throughout the code

    match user:
        case "add" | "Add":         # | syntax is used for 'or'
            todo = input("Add names :")
            todos.append(todo)
        case "show" | "Show":
            for item in todos:      # item is a variable after for.loop and we can play with it
                item = item.upper()
                print(item)
        case "exit" | "Exit":
            break
        case whatever:               #we can add variable after case.
            print("type add or show or exit")
print("Thanks !!")



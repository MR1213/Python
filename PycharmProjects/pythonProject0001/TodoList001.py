todo = ["1", ]

while True:
    ask_todo = input(int("(1)View Todo list, (2)Add Item, (3)Remove Item, (4)Exit: ")
    if ask_todo == 1:
        print(todo)
    elif ask_todo == 2:
        add_todo = input(str("What would you like to add to the Todo list? "))
    elif ask_todo == 3:
        print(todo)
        remove_item = input(int(print("Which item do you want to remove? ")))

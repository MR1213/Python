options = """\
    (1) View Wish List (2) View Item (3) Add Item
    (4) Delete Item (5) Exit
"""
wishlist = {
    "Playstation 5": 500,
    "Xbox 1": 300,
    "Gaming PC": 1500,
    "Gaming Mouse": 50,
    "Gaming Headset": 50,
    "Gaming Keyboard": 120,
    "Nintendo Switch": 200,
    "Gaming monitor": 150,
    "Mouse Pad": 25,
    "Gamer Snacks": 5,
    "Gamer Drinks": 5,
    "LED lights": 25,
}
while True:
    choice = int(input(options))
    if choice == 1:
        print(wishlist)
    elif choice == 2:
        view_wishlist = int(input("Which item do you want to see? "))
        if view_wishlist in wishlist:
            print(wishlist)
        else:
            print("That doesnt exist... ")
    elif choice == 3:
        add_wishlist = str(input("What do you want to add to the wishlist? "))
        wishlist.append(add_wishlist)
    elif choice == 4:
        delete_wishlist = int(input("Which item do you want to delete? "))
        wishlist.pop(delete_wishlist)
    elif choice == 5:
        break
    else:
        print(f"{choice} is not a valid option")
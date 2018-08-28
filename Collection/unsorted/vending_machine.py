sodas = ["Pepsi","Cherry","Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some CHIPS or a CANDY?").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack == candy.pop()
        else:
            print("Sorry, I didn't understand that,")
            continue
    except IndexError:
        print("Sorry, we're all out of {}".format(choice))
    else:
        print("Here's your {}: {}".format(choice,snack))



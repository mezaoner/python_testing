#Will run forever until break
import os
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("where should I add {}?\n"
                        "Press ENTER to add to the end of the list \n"
                        "> !".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1,item)
    else:
        shopping_list.append(item)
    show_list()

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter DONE to stop adding items
enter QUIT to quit
enter HELP to show this help
enter LIST to show your list
enter REMOVE to delete an item from the list
""")

def show_list():
    clear_screen()
    print("Here's your shopping list:")
    
    for index,item in enumerate(shopping_list, start = 1):
        print("{}. {}".format(index,item))      
    print("-" * 20)

def remove_from_list():
    show_list()
    remove = input("What should I remove sir? ")
    try:
        shopping_list.remove(remove)
    except ValueError:
        pass
    show_list()

show_help()
while True:
    new_item = input("> ")
    if new_item.upper == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "LIST":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        continue
    else:
        add_to_list(new_item)
        continue
show_list()
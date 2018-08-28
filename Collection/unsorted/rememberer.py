import sys

def rememberer(thing):
    #open file
    with open("database.txt", "a") as file:
        #write thing to file
        file.write(thing+"\n")

def show():
    with open("database.txt") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    if sys.argv[1].lower() == "--list":
        show()
    else:
        rememberer(input("What should i remember?: "))
books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]
def wish_display(heading, wishes):
    print(heading + ":")
    items = wishes.copy()
    suggested_gift = items.pop(0)
    print("=====>", suggested_gift, "<=====")
    for item in items:
        print("* " + item)
    print()

wish_display("Books",books)

wish_display("Spill",video_games)

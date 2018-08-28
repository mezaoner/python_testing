musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
bandlist = []
for members in musical_groups:
    if(len(members) == 3):
        bandlist.extend(members)
memberlist =", ".join(bandlist)
print(memberlist)

def disemvowel(word):
    wordlist = list(word)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for letter in wordlist.copy():
        if letter.lower() in vowels:
            wordlist.remove(letter)
    word = "".join(wordlist)
    return word

print(disemvowel(input("please input the word: ")))

def reverse_evens(my_list):
    return my_list[::2][::-1]

def sillycase(data_in):
    half = round(len(data_in) / 2)
    first = data_in[:half].lower()
    second = data_in[half:].upper()
    return first + second

    def word_count(string):
    string = string.lower()
    word_dict = {}
    word_list = string.split()
    for sel_word in word_list:
        count = 0
        for word in word_list:
            if sel_word == word:
                count +=1
        word_dict[sel_word] = count
    return word_dict

     





def num_teachers(dicty):
    integer = 0
    for teachers in dicty.items():
        integer += 1
    return integer
def num_courses(dict):
    counter = 0
    for courses in dict:
        course_teacher = (dict[courses])
        for total in course_teacher:
            counter += 1
    return counter
def courses(dict):
    courselist = []
    for courses in dict:
        course_teacher = (dict[courses])
        for course in course_teacher:
            courselist.append(course)
    return courselist
def most_courses(dict):
    max_count = 0
    counter = 0
    champ = "nobody"    
    for courses in dict:
        counter = 0
        course_teacher = (dict[courses])
        for course in course_teacher:
            counter = counter + 1 
            print("Counter: {}".format(counter))
            if counter > max_count:
                max_count = counter
                print("maxcount: {}".format(max_count))
                champ = courses
    return champ

def stats(dict):
    max_count = 0
    counter = 1
    thelist = []
    test_for_teacher = "none"    
    for teacher in dict:
        counter = 1
        course_teacher = (dict[teacher])
        for course in course_teacher: 
            teacher_nr = 0
            if teacher == test_for_teacher:
                counter += 1
                thelist[teacher_nr] = [teacher,counter]
            else:
                thelist.extend([teacher,counter])
                test_for_teacher = teacher
    teacher_nr =+ 1
    return thelist

#"bedre "
def stats(dic):
    outer_list = []
    for key in dic:
        inner_list = []
        inner_list.append(key)
        inner_list.append(len(dic[key]))
        outer_list.append(inner_list)
    return outer_list

dictionary = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics',"egvil","vinna"],'Kenneth Love': ['Python Basics', 'Python Collections',"Nomode Basics"]}


 for index, letter in enumerate("abcdefghijklmnopqrstuvqxyz"):
     print("{} : {}".format(index+1,letter)

def stringcases(stringin):
    return(stringin.upper(), stringin.lower(),stringin.title(),stringin[::-1])

stringcases("halla Ludder, e du THUG")

def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        output += (iter1[i], iter2[i]),
    return output

def covers(topic):
    output = []
    for key,value in COURSES.items():
        if value & topic:
            output.append(key)
    return output

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    output = []
    for key,value in COURSES.items():
        if value & topic:
            output.append(key)
    return output
def covers_all(topic):
    output = []
    #key equals course names, value equals topics
    for key,value in COURSES.items():
        if topic <= value:
            output.append(key)
    return output

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)
box = []
for item in TILES:
    if item == "||":
        print("{}".format("".join(box)))
        box = []
    else:
        box.append(item)

class RaceCar:


    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= (length * 0.125)
        self.laps += 1


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern


    def __str__(self):
        output = ""
        for attr in self.pattern:
            if attr == ".":
                output += "dot"
            if attr == "_":
                output += "dash"
            output += "-"
        return output[:-1]

class Liar(list):
    def __init__(self, *arg):
        self.list = []
    def __len__(self):
        super().__len__()
        length = len(self.list) + 1
        return length


listami = Liar()
listami.list = [1,2,3,4]

print(len(listami))

##############################################Jævla drittoppgaven

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, my_string):
        correct_list = []
        dash_dots = my_string.split("-")
        for i in dash_dots:
            if i == "dash":
                correct_list.append("_")
            elif i == "dot":
                correct_list.append(".")
        correct_pattern = Letter(pattern=correct_list)
        return correct_pattern


class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)
##############################################Jævla drittoppgaven END!!!!

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.width + self.length) * 2

##################Enda en #dice
from Collection.Dice.dice import D20

class Hand(list):

    def __init__(self, size=0, die_class=D20):
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @classmethod
    def roll(cls, size=2):
        return cls(size=size)

    @property
    def total(self):
        import datetime

        def to_string(dt):
            return dt.strftime("%d %B %Y")

        def from_string(dt, strfstring):
            return datetime.datetime.strptime(dt, strfstring)

import datetime
starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(integer, string):
    if string == "minutes":
        return starter + datetime.timedelta(minutes=integer)
    elif string == "hours":
        return starter + datetime.timedelta(hours=integer)
    elif string == "days":
        return starter + datetime.timedelta(days=integer)
    elif string == "years":
        return starter + datetime.timedelta(days=integer*365)
    else:
        pass


### finding shite
import re

def phone_numbers(streng):

    return re.findall(r"\d[3}\-\d[3}\-\d[4}", streng)


def find_words(count, streng):
    return re.findall(r'\w' * count + '\w*', streng)


import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r"""
                    (?P<email>[-\w\d.+]+@[-\w\d.]+)  #email
                    (,\s
                    (?P<phone>\d{3}-\d{3}-\d{4}))    #phone
                    """, string, re.X | re.M)
twitters = re.findall(r"(?P<twitter>@[\w]{3,})$", string, re.X | re.M)

### MEKKASJÆL

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.findall(r""
                    r"^(?P<last_name>\b[\w+\s*]+\b)"
                    r",\s"
                    r"(?P<first_name>\b[\w\s*]+\b)"
                    r"\:\s"
                    r"(?P<score>[ \d]+)$"
                    r"", string, re.X | re.M)
class Player:
    def __init__(self, first_name=None, last_name=None, score=None):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score


## scanner for filer med ext fra kjøremappe:
import glob

for filename in glob.iglob('**/*.py', recursive=True):
     print(filename)

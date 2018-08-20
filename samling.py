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
    
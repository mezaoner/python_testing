def packer(name=None,**kwargs):
    print(kwargs)

def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("Hi {} {}".format(first_name,last_name))
    else:
        print("Hi Noname")

packer(name="Martin", naaum = 2354, spanish_inquisition = True)
unpacker(**{"last_name":"Love","first_name":"Kenneth"})

course_minutes = {"Python basics": 232, "Django Basics": 237, "Flask basics": 189, "Java basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course,minutes))
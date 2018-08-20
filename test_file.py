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
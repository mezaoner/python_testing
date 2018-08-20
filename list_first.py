#first file for listy
#meeting
attendees= ["Ken","Elena","Treasure"]
attendees.append("Ashlee")
attendees.extend(["James","Guil"])
optional_attendees = ["Benji","Jenbi"]
potential_attendees = attendees + optional_attendees
print("There are {} potential attendees ".format(len(potential_attendees)))

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("To : " + to_line)
print("Cc: " + cc_line)
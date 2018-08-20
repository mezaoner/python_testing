#fil en, the beginning
first_name = input("What is your first name?  ")
print("Hello,",first_name,"!")
if first_name == "Martin":
    print(first_name,"is learning Python")
elif first_name == "Stig":
    print (first_name," lærer ingenting")    
else:
    age = int(input("How old are you? "))
    #just in case young user that cannot read
    if age <= 6:
        print("wow you're {} and reading already".format(age))
    print("You should learn Python {}!".format(first_name))
print("Have a great day {}!".format(first_name))
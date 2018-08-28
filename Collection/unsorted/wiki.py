import datetime

answer_format = "%m/%d"
link_format = "%b_%d"
link = "https://en.wikipedia.org/wiki/{}"

while True:
    answer = input("What date would you like, please use MM/DD format, enter Q to quit")
    if answer.upper() == "Q":
        break

    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("invalid date, try again")
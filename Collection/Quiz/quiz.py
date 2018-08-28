import datetime
import random

from Collection.Quiz.questions import Add, Multiply

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        #generate 10 random questions with number from 1 to 10
        for _ in range(10):
            num1 = (random.randint(1,10))
            num2 = (random.randint(1,10))
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)
        #add these questions into self.questions

    def take_quiz(self):
        input("Press enter to start")
        self.start_time = datetime.datetime.now()
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()

        return self.summary()

    def ask(self, question):
        correct = False
        #log start time
        question_start = datetime.datetime.now()
        #capture answer
        answer = input(question.text + "=")
        #check answer
        if answer == str(question.answer):
            correct = True
        #log end time
        question_end = datetime.datetime.now()
        #send  true/ false and elapsed time
        return correct, question_end - question_start
    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        #print how many right out of 10
        print("you got {} out of {} right".format(
            self.total_correct(), len(self.questions)
        ))
        #Print total quiz time
        print("it took you {} seconds total".format(
            (self.end_time-self.start_time).seconds
        ))

Quiz().take_quiz()

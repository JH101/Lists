# Jamie Hilton
# 13/01/15
# Countries quiz extended

import random

column1 = ["England", "USA", "Germany", "Italy", "Poland", "Canada", "Scotland", "Ireland", "France", "Japan"]

column2 = ["London", "Washington", "Berlin", "rome", "Warsaw", "Ottowa", "Edinburgh", "Dublin", "Paris", "Tokyo"]

right = 0

for count in range (5):
    city = random.randrange(8)
    guess = False

    while guess == False:

        answer = column2[city]

        country = column1[city]

        question = input("Please enter the capital of {0}: ".format(country))

        if question == answer:

            print("That is the right answer")

            guess = True

            right = right + 1

print("You scored {0}/5".format(right))

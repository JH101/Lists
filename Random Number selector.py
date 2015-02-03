# Jamie Hilton
# 13/01/15
# Random Number selector

import random 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
def generator(numbers):
    for count in range(6):
        number = 0
        while number == 0:
            random_number = random.randrange(18)
            number = numbers[random_number]
        numbers[random_number] = 0
        print(number)
    print(numbers)

#Main Program
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
generator(numbers)
    


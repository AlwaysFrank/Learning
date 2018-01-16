#!/user/bin/python3
#-*-coding:UTF-8-*-

import random

start = 1
end = 500
number = random.randint(start, end)

guess = 0
while True:
    num_input = input("Please input a number between %d and %d\n"%(start, end))
    guess += 1

    if not num_input.isdigit():
        print('Please input a digital number.')
    elif int(num_input) < start or int(num_input) > end:
        print('Please choose number between %d and %d.'%(start, end))
    else:
        if number == int(num_input):
            print('Congratulations, the number is %d. You already try %d time%s'
                  %(number, guess,  ''if guess == 1 else's' ))
            break
        elif number > int(num_input):
            print('Please try some bigger number.>')
        elif number < int(num_input):
            print('Please try some smaller number.<')
        else:
            print('Some interesting things were happend, Please try to contact me as soon as possible.')

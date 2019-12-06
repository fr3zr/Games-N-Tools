#!/usr/bin/env python

"""Docstring of Application"""

print('Hello, what is your name?')
myName = input('My name is : ')
print('Hello, ' + myName +'!')
answer = 'y'
while answer == 'y':
    tries = 0
    num = random.randint(1,20)
    numGuessed = 0
    while numGuessed != num:
        tries = tries + 1
        if tries == 1:
            print('I choose a number between 1 and 20')
        elif tries > 1:
            if numGuessed > num:
                print('My number is smaller than the one you guessed')
            elif numGuessed < num:
                print('My number is bigger than the one you guessed')
        print('What number are you guessing?')
        numGuessed = input('My guess is: ')
        numGuessed = int(numGuessed)
        if numGuessed < 1 or numGuessed > 20:
            print('I said a number between 1 and 20')
    if numGuessed == num:
        tries = str(tries)
        print('You guessed the number correctly')
        print('It took you ' + tries + ' tries to guess the number')
        answer = input('Do you want to try again? y/n : ')
    else:
        print('You somehow created a error, please tell the administrator the steps to reproduce it')
print('Exiting Program')
sys.exit()

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = input("Enter the calculation type and numbers separated by space: ")
    tokens = user_input.split(" ")
    numbers = []
    test = 0
    for token in tokens[1:]:
        try:
            numbers.append(float(token))
        except:
            print("You did not enter numbers.")
            test = 1
            break
    
    number2_list = ['+', '-', '*', '/', 'pow', 'mod']

    if tokens[0] in number2_list:
        if len(numbers) < 2:
            print('Not enough numbers.')
            test = 1
    number1_list = ['square', 'cube']

    if tokens[0] in number1_list:
        if len(numbers) < 1:
            print ('Not enough numbers.')
            test = 1
            
    if test == 1:
        continue

    if tokens[0] == 'q':
        break
    elif tokens[0] == '+':
        print(add(numbers[0],numbers[1]))
    elif tokens[0] == '-':
        print(subtract(numbers[0], numbers[1]))
    elif tokens[0] == '*':
        print(multiply(numbers[0], numbers[1]))
    elif tokens[0] == '/':
        print(divide(numbers[0], numbers[1]))
    elif tokens[0] == 'square':
        print(square(numbers[0]))
    elif tokens[0] == 'cube':
        print(cube(numbers[0]))
    elif tokens[0] == 'pow':
        print(power(numbers[0], numbers[1]))
    elif tokens[0] == 'mod':
        print(mod(numbers[0], numbers[1]))
    else:
        print("Incorrect command.")




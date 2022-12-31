#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# negative number mod 10 is not what you'd expect
# 'num' created to avoid modifying 'number'
if (number < 0):
    num = abs(number)
    last_digit = num % 10
    last_digit *= -1
else:
    last_digit = number % 10

if (last_digit > 5):
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif (last_digit < 6 and last_digit != 0):
    print(f'Last digit of {number} is {last_digit} and is less than\
 6 and not 0')
elif (last_digit == 0):
    print(f'Last digit of {number} is {last_digit} and is 0')

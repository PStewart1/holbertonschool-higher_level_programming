#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(repr(number)[-1])
if number < 0:
    num *= -1
print("Last digit of {} is {} and is ".format(number, num), end='')
if num > 5:
    print("greater than 5")
elif num == 0:
    print("0")
else:
    print("less than 6 and not 0")

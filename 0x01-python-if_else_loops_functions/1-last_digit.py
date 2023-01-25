#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number) % 10
if number < 0:
    lastD = -lastD
print("Last digit of {} is {} and is ".format(number, lastD), end="")
# Test for print output
if lastD > 5:
    print("greater than 5")
elif lastD == 0:
    print("0")
else:
    print("less than 6 and not 0")

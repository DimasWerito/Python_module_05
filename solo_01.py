"""
Create a timer program that will take the number of seconds as input, and countdown to 0.
"""


# take the number as input
number = int(input())

#use a while loop for the countdown
while number >= 0:
    print(number)
    number -= 1
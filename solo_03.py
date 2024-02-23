"""
A smart parking lot displays different messages to the visitor 
based on the number of available spaces.

 

Task

Complete the program to inform the user about available spaces in the parking lot


"""


# Take the number of available spaces as an input
spaces = int(input())

# Display message if spaces are available
if spaces > 0:
    print("Available spaces")

# Display a different message if spaces are not available
else:
    print("Sorry, the parking lot is full")
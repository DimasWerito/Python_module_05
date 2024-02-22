"""
Imagine you are a scientist looking at a new type of cell under the microscope. 
This type of cell divides itself into 2 daughter cells every 24 hours, 
meaning that the cell population duplicates every day.

Task

Complete the code to take the initial cell population
 and the number of days you are observing the cells to calculate 
 the cell population at the end of each day in the following format
"""


# take the initial cell population as input
cells = int(input())

# take the number of days as input
days = int(input())

# initialize the day counter
counter = 1

#complete the while loop
while counter <= days:
  cells = cells * 2
  # Daily message
  print("Day " + str(counter) + ": " +str(cells))
  counter = counter + 1
"""
This list is for the breakfast menu on a hotel’s website:

breakfasts = [
  'Donuts', 'Waffles', 'Yogurt', 
  'Burrito', 'Toast']
PY
The Chef decided to replace one of the options with "Pancakes".

The given code takes the index of the option to be replaced as input.

 

Task

Complete the program to replace the menu item and display the new menu on the screen.
"""


#the list of breakfasts
breakfasts = [
  'Donuts', 'Waffles', 'Yogurt', 
  'Burrito', 'Toast']

#index of the item to be replaced
item = int(input())

#replace that item with "Pancakes"
breakfasts[item] = "Pancakes"

#display the updated list
print(breakfasts)
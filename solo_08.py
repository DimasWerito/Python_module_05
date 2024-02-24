"""
Adam uses an app that records how many steps he takes each day. 
Here are his step counts for the past week:

steps = [1513, 5035, 7891, 1212, 2534, 4648, 3785]
PY
Adam wants to review his activity over the past 3 days.

 
Task

Write the code to make a slice and output Adam’s step counts for the last 3 days (the last 3 items in the list).
"""


#step counts for the past week
steps = [1513, 5035, 7891, 1212, 2534, 4648, 3785]

#make a slice for the last 3 days
last_3 = steps[4:]

#display the slice
print(last_3)
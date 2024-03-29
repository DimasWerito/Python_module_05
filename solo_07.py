"""
In a relay race competition, there are 6 participants listed as follows:

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
PY
Players are divided into three groups of two based on the following logic: 
the first two participants form the first group, 
the 3rd and 4th participants form the second group, 
and the 5th and 6th participants form the third group.

Task

Complete the code to perform the necessary slicing and display the groups on the screen.
"""


players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

#Create 3 lists with 2 players each
#Use slicing to create a list for Group 1
g1 = players[0:2]

#Use slicing to create a list for Group 2
g2 = players[2:4]

#Use slicing to create a list for Group 3
g3 = players[4:6]

print("Group 1:")
#display the 1st group
print(g1)

print("Group 2:")
#display the 2nd group
print(g2)

print("Group 3:")
#display the 3rd group
print(g3)
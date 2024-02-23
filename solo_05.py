"""
A game machine has 5 games installed on it, represented in this list:

games = ['Soccer', 'Tic Tac Toe', 
'Snake', 'Puzzle', 'Rally']
PY
The code that you're about to see takes a number as input, which indicates the choice index.

 
Task

Complete the program to output the game 
from the list that corresponds to that index.
"""


#installed games
games = [
  'Soccer', 'Tic Tac Toe', 'Snake',
  'Puzzle', 'Rally']

#taking player's choice as a number input
choice = int(input())

#output the corresponding game
print(games[choice])
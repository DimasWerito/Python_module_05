"""
Imagine you’re working on a program to manage customer support queues.

The queue is a list in the code. 

 

Task

Write a program to take a name as input, add it to the end of the queue, and output the resulting list.
"""


queue = ['John', 'Amy', 'Bob', 'Adam']

#take an input
name = input()

#add the taken value to the end of the queue
queue.append(name)

#display the updated queue
print(queue)
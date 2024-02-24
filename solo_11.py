"""
Imagine you need to calculate the shipping cost for customer orders based on the weight of the packages.

The cost per kilogram is $5.


Task

Complete the shipping_cost() function to take the weight as an argument, calculate the shipping cost based on the weight, and display it in the given format.

The function call is already done.

"""


#taking the weight as input
weight = int(input())

#complete the function
def shipping_cost(weight):
     print(weight * 5)

#function call
shipping_cost(weight)
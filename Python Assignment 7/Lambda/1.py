# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Sample Output: 25 48 

a = int(input("Enter a number: "))

x = lambda x : x + 15
print(x(a))

z = lambda x,y: x*y
print(z(a, 4))
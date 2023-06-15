# 6)  Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda 
# Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
# Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190] 

a = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 

x = list(filter(lambda y: y%19==0 or y%13==0, a ) )
print("Numbers of the above list divisible by nineteen or thirteen:", x)
# 8.  Write a Python program to sum all the items in a dictionary.


def my_fun(my_dict):
    sum=0
    for values in my_dict.values():
        sum+=values
    return sum


my_dict = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50, "F": 60}
res= my_fun(my_dict)
print("The sum of items is:", res)

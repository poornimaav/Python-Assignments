# 9. Write a Python program to multiply all the items in a dictionary.

def my_fun(my_dict):
    mul_values=1
    for keys, values in my_dict.items():
        mul_values*=values
    return mul_values


my_dict = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50, "F": 60}
res= my_fun(my_dict)
print("The product of items is:", res)
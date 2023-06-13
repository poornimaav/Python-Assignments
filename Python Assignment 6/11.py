# 11. Write a Python program to sort a dictionary by key.


my_dict = {'d':70, 'a': 30, 'e':90, 'r': 12, 's':45, 'i':20}

res=dict(sorted(my_dict.items()))

print(res)
# 12. Write a Python program to get the maximum and minimum value in a dictionary. 

my_dict = {'d':70, 'a': 30, 'e':90, 'r': 12, 's':45, 'i':20}

# print("Maximum value: ", max(my_dict.values()))
# print("Minimum value: ", min(my_dict.values()))
min= my_dict['d']
max= my_dict['d']

for key in my_dict.keys():
    if my_dict[key] > max:
        max= my_dict[key]
    elif my_dict[key]<min:
        min=my_dict[key]

print("Maximum value: ", max)
print("Minimum value: ", min)
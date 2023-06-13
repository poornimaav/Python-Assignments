# 13. Write a Python program to remove duplicates from Dictionary.

my_dict = {'d':70, 'a': 30, 'e':90, 'r': 12, 's':45, 'i':20, 'a':60, 'e':20}
new_dict={}
for keys in my_dict.keys():
    if keys in new_dict.keys():
        continue
    else:
        new_dict[keys]=my_dict[keys]
    

print(new_dict)
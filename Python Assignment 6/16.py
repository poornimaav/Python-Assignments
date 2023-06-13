# 16. Write a Python program to find the highest 3 values in a dictionary.


my_dict = {'d':70, 'a': 30, 'e':90, 'r': 12, 's':45, 'i':20}
res = {}

n=0
while n<3:
        max_key=max(my_dict, key=my_dict.get)
        res[max_key]=my_dict[max_key]  
        del my_dict[max_key]
        n+=1
print(res)


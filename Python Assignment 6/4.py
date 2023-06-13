# 4. Write a Python script to check if a given key already exists in a dictionary. 


def key_check(my_dict, key):
    if key in my_dict:
        return True
    else:
        return False


my_dict= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key=5
res=key_check(my_dict,key)

if res==True:
    print("The key", key, "exits in my_dict dictionary" )
else:
    print("The key does not exist")
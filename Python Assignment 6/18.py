# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


# my_list= [{1,2},{},{}]
my_list= [{},{},{}]

def my_fun(my_list):
    for i in my_list:
        if len(i)!=0:
            return False

    return True

res=my_fun(my_list)
print(res)
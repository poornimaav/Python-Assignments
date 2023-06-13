# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

def sort_by_value(dict1, reverse=False):
    sort_dict=dict(sorted(dict1.items(), key=lambda item:item[1], reverse=reverse))
    return sort_dict

dict1={'a':10, 'b':9, 'c':3, 'd':8, 'e':1}
sort_asc=sort_by_value(dict1)
sort_dsc=sort_by_value(dict1, reverse=True)

print("Ascending order: ", sort_asc)
print("Descending order: ", sort_dsc)

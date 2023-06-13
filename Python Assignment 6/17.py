# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y


dic1 = {'key1': 1, 'key2': 3, 'key3': 2}

dic2 = {'key1': 1, 'key2': 2}
 
for key,value in dic1.items():
    if key in dic2 and dic2[key]==dic1[key]:
        print(key, ":", value, "is present in both dic1 and dic2")

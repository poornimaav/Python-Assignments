# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 

a = "PaceWisd0m"
res = lambda s: all([any(c.isupper() for c in s), any(c.islower() for c in s), any(c.isdigit() for c in s),len(s) >= 10 ])

if res(a):
    print("valid string")
else:
    print("Invalid string")
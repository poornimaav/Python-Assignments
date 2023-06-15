# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 
a=['red', 'black', 'white', 'green', 'orange']
sub="ack"
res= list( filter(lambda x: sub in x, a))
print(res)
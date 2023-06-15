# 7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#  Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]] 


list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 

res = sorted(list1, key=lambda x : sum(x))
res1 = sorted(list2, key=lambda x : sum(x))
print("Sort the said matrix in ascending order according to the sum of its rows: ",res)
print("Sort the said matrix in ascending order according to the sum of its rows: ",res1)
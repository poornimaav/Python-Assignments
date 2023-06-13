#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def my_fun(n):
    res={}
    for i in range(1,n+1):
        res[i]=i*i
    return res

n=5
res=my_fun(n)
print(res)
# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 


class  Pair_element():
    def pair(self, numbers):
        list1 = []

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                for k in range(j+1, len(numbers)):
                    if numbers[i]+numbers[j]+numbers[k]==0:
                        list1.append([numbers[i], numbers[j], numbers[k]])
        return list1

res = Pair_element() 
numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
print(res.pair(numbers))

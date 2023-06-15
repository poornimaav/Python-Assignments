# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 


class  Pair_element():
    def pair(self, numbers, target):
        list1 = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j]==target:
                    list1.append((i, j))
        return list1

res = Pair_element()
numbers = [90, 20,10,40,50,60,70]
print("The indices are :", res.pair(numbers, 50))
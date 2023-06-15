# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 


class Sub_Gen:
    def unique_subsets(self, nums):
        subsets = [[]]  
        for num in nums: 
            new_subsets = [] 
            for subset in subsets: 
                new_subsets.append(subset + [num]) 
            subsets.extend(new_subsets) 
        return subsets


nums = [4, 5, 6]

res = Sub_Gen()
print(res.unique_subsets(nums))
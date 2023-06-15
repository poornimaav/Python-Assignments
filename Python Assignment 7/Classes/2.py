# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 

class Validity:
    def is_valid(self, str1):
        list1 = []
        para_char = { "(" : ")" , "{" : "}" , "[" : "]" }
        for paranthesis in str1:
            # print(paranthesis)
            if paranthesis in para_char:
                list1.append(paranthesis)
            elif len(list1)==0 or para_char[list1.pop()]!=paranthesis:
                return False
        return len(list1)==0

res = Validity()
print(res.is_valid("()"))
print(res.is_valid("(){}[]"))
print(res.is_valid("[)"))
print(res.is_valid("({[)"))
print(res.is_valid("{{{"))

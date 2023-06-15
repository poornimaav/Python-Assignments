# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

class reverse():
    def reverse_string(self, str1):
        str2 = str1.split()
        str2= str2[::-1]
        str3 = ' '.join(str2)
        return str3

res = reverse()
str1 = 'hello .py'
print(res.reverse_string(str1))
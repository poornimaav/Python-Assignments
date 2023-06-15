# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order 

class reverse_string():
    def get_string(self):
        string = input("enter a string: ")
        return string

    def print_string(self, string):
        reversedString = string[::-1]
        return reversedString

output = reverse_string()

string = output.get_string()
res = output.print_string(string)
print(res)
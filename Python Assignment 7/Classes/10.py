# 10) Write a Python program to get the class name of an instance in Python.


class MyClass:
    pass

instance = MyClass()
print("Class name:", instance.__class__.__name__)

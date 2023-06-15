# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.



class Circle():
    def find_area(self, r):
        return r**2

    def find_perimeter(self, r):
        return 2*3.14*r

res = Circle()
r= 5
print("Area: ", res.find_area(r))
print("Perimeter: ", res.find_perimeter(r))
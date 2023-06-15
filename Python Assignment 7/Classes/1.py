# 1) Write a python class to convert an integer into a roman numeral and viceversa

class Converter:
    def __init__(self):
        self.roman_number = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
    
    def num_to_roman(self,num):
        roman_num= ''

        for rom, number in self.roman_number.items():
            while (num >= number):
                roman_num += rom
                num -= number
        return roman_num

    def roman_to_num(self,roman):

        n = len(roman)
        i=n-1
        num = 0
        while i >= 0:
            if i < n-1 - 1 and self.roman_number[roman[i]] < self.roman_number[roman[i+1]]:
                num-= self.roman_number[roman[i]] 
                print(num)
            else:    
                num+= self.roman_number[roman[i]] 
            i-=1
        return num


result = Converter()

print(result.roman_to_num('DCM'))
print(result.num_to_roman(1600))
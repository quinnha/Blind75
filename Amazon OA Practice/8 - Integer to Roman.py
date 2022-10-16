
# 7 -> VII

def intToRoman(num):
    
    out = ""

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    for i in range(len(val)):
        
        while num >= val[i]:
            out += rom[i]
            num -= val[i]
    return out
    
print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))



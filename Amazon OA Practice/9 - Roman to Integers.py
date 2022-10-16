
def romanToInt(s):
    dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C":100, "XC": 90, "L": 50, "XL": 40, "X": 10, "V": 5, "IV" : 4, "I": 1}

    out = 0

    for i in range(len(s)-1, -1, -1):
        if i != len(s) - 1 and s[i] == "I":
            if s[i + 1] == "V" or s[i + 1] == "X": out -= 1
            else: out += 1
        elif i != len(s) -1 and s[i] == "X":
            if s[i + 1] == "L" or s[i + 1] == "C": out -= 10
            else: out += 10
        elif i != len(s) -1 and s[i] == "C":
            if s[i + 1] == "D" or s[i+ 1] == "M": out -= 100
            else: out += 100
        else:
            out += dic[s[i]]

    return out

print(romanToInt("LVIII"))
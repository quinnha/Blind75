import re
def myAtoi(s):

    i = 0
    flag = False
    nums = "0123456789"
    while True:
        if s[i] != " ":
            break
        else:
            i += 1
    if s[i] != "+" and s[i] != "-" and s[i] not in nums: return 0

    s = s[i:]
    if s[0] == "-": 
        flag = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
        
    i = 0
    while True:
        if s[i].isnumeric(): 
            i+= 1
            if i == len(s) -1: break
        else:
            break
    
    s = s[0:i+1]
    s = re.sub('\D',"", s)
    num = int(s)

    if flag: num *= -1

    if num > (2**31) -1: num = 2**31 -1
    elif num < -(2**31): num = -(2**31)

    return num

print(myAtoi("+-987"))


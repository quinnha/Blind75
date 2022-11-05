def reverse(self, x: int) -> int:
        flag = False
        s = str(x)
        if s[0] == "-": 
            flag = True
            s = s[1:]
        s = int(s[::-1])
        if flag: s *= -1
        if s > 2**31 -1 or s < -2**31: return 0
        return s
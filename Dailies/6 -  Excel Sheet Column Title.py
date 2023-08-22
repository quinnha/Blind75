# Day 6, Aug 21, https://leetcode.com/problems/excel-sheet-column-title/


def convertToTitle(columnNumber):
    n = columnNumber
    ans = []
    while n > 0:
        n -= 1
        curr = n % 26
        n = int(n / 26)
        ans.append(chr(curr + ord("A")))

    return "".join(ans[::-1])


print(convertToTitle(52))

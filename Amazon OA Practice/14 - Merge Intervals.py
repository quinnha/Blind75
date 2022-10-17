
def merge(intervals):

    # sort by first number
    s = sorted(intervals, key = lambda x:x[0])
    
    out = [s[0]]
    
    for i in range(len(s)):
        if s[i][1] >= out[-1][0]: out[-1][1] == max(s[i][1], out[-1][1])
        else: out.append(s)

    return out



print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4]]))
print(merge([[1,4], [0,4]]))
print(merge([[1,4], [2,3]]))

t = [1,2,3,4,5,6,7]


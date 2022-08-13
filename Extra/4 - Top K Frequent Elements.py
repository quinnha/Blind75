# add numbers with freq into a dic, and pick the max out 
def topKFrequent (nums, k):

    out = []
    d = {}
    for i in set(nums):
        d[i] = nums.count(i)

    for i in range (k):
        maxd= max(d, key=d.get)
        out.append(maxd)
        del d[maxd] # delete so it doesnt get picked again!
    
    return out

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
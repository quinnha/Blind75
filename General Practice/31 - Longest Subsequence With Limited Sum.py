from collections import bisect
from bisect import bisect_right
def answerQueries(nums, queries):
        nums.sort()
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1]+n)
        res = []
        for q in queries:
            indx = bisect_right(preSum,q)
            res.append(indx-1)
        return res


answerQueries([1,2,3,4],[123])
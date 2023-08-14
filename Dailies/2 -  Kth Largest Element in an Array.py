# Day 2, Aug 14, https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


def findKthLargest(nums, k):
    nums = [num * -1 for num in nums]
    heapq.heapify(nums)
    for i in range(k - 1):
        heapq.heappop(nums)
    print(list(nums))

    return list(nums)[0] * -1


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))

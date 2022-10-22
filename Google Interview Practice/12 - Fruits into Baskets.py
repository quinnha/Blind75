from collections import Counter
def totalFruit(tree):
    l, nums, res = 0, Counter(), 0
    for r in range(len(tree)):
        nums[tree[r]] += 1
        while len(nums) > 2:
            nums[tree[l]] -= 1 
            if not nums[tree[l]]:
                nums.pop(tree[l])
            l += 1
        res = max(res, r - l + 1)
    return res
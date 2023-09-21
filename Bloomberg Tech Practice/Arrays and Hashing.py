# two sum

def twoSum(nums, target):

    dic = {}
    for i, num in enumerate(nums):
        dic[target-num] = i

    for i, num in enumerate(nums):
        if num in dic.keys() and i != dic[num]: return [i, dic[num]]
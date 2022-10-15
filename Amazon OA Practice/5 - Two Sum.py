
def twoSum(nums, target):
    dic = {}

    for index, num in enumerate(nums):
        if num in dic.keys():
            return [dic[num], index]
        else:
            dic[target-num] = index
    return -1

print(twoSum([2, 7, 11, 15], 9))
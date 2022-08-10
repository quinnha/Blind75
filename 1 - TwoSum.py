# Math is num2 = target - num1
# so store target - num1 as the key, and num1's index as the value
# create hash/dict, and if num2 (iterating num) is a key (target - num1) there is twosum

def twoSum (nums, target):

    d = {}
    for i in range (len(nums)):
        
        if nums[i] in d: 
            return [d[nums[i]], i]
        else:
            d[target-nums[i]] = i
      
    return None 
        
    



print (twoSum([3,3,4], 6)) 
print (twoSum([3,5,4], 8)) 

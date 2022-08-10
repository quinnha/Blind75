# basically keep track of your maximum and your minimum, because they can switch at any time
# when you get a negative, switch em, because it reverses

def maxProduct (nums): 
    
    minimum = maximum = return_maximum = nums[0]
    
    for num in nums [1:]:
        if num < 0: minimum, maximum = maximum, minimum 

        maximum = max(maximum*num, num) # if larger, apply 
        minimum = min(minimum*num, num) # if smaller (larger negative), apply

        return_maximum = max (return_maximum, maximum)

    return return_maximum
       



print(maxProduct([2,3,-2,4]))
print(maxProduct([-3, -1, -1]))
print(maxProduct([0,2]))
print(maxProduct([0,3, 4, 0, 4,7]))
print(maxProduct([-2]))
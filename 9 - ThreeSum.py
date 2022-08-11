
# def threeSum(nums):

#     res = set()

# 	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
#     n, p, z = [], [], []
#     for num in nums:
#         if num > 0:
#             p.append(num)
#         elif num < 0: 
#             n.append(num)
#         else:
#             z.append(num)

#     #2. Create a separate set for negatives and positives for O(1) look-up times
#     N, P = set(n), set(p)

#     #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
#     #   i.e. (-3, 0, 3) = 0
#     if z:
#         for num in P:
#             if -1*num in N:
#                 res.add((-1*num, 0, num))

#     #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
#     if len(z) >= 3:
#         res.add((0,0,0))

#     #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
#     #   exists in the positive number set
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             target = -1*(n[i]+n[j])
#             if target in P:
#                 res.add(tuple(sorted([n[i],n[j],target])))

#     #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
#     #   exists in the negative number set
#     for i in range(len(p)):
#         for j in range(i+1,len(p)):
#             target = -1*(p[i]+p[j])
#             if target in N:
#                 res.add(tuple(sorted([p[i],p[j],target])))

#     return res

# 3 Poitner Method (better)

# so sort, and then keep 3 pointers -> iterate through the first left pointer, and do the
# sorted two sum method to find a match 
def threeSum(nums):

    nums = sorted(nums)
    target = 0

    res = []

    for first_left in range (len(nums) -1): #setting first pointer to move thru lsit
        
        left = first_left + 1 #setting the values for left and left based off first_left
        right = len(nums)-1

        while left < right: #twosum sorted method

            if nums[first_left] + nums[left] + nums[right] > target:
                right -= 1
            elif nums[first_left] + nums[left] + nums[right] < target:
                left += 1
            else:
                if [nums[first_left], nums[left], nums[right]] not in res: #prevent dups
                    res.append([nums[first_left], nums[left], nums[right]])
                right -= 1
                left += 1
        
    return res
    return -1



    return nums

print (threeSum([-1, 0, 1, 2, -1, -4]))
print (threeSum([0,0,0]))
print (threeSum([0,2,1]))





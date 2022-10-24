# binary search for sorted list


def binarySearch(nums, k):

    l = 0
    r = len(nums) -1    
    
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == k:
            return mid
        elif nums[mid] > k:
            r = mid - 1
        elif nums[mid] < k:
            l = mid + 1
    
    return -1

print(binarySearch([1,2,3,4,5,6,7], 7))
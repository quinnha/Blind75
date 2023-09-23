# is palindrome
def isPalindrome(s):
    parsed = "".join(x.lower() for x in s if x.isalnum())

    # easy way
    # return parsed == parsed[::-1]

    left = 0
    right = len(parsed) - 1

    while left < right:
        if parsed[left] != parsed[right]:
            return False
        left += 1
        right -= 1
    return True


# three sum
def threeSum(nums):
    ret = []
    nums = sorted(nums)

    for left in range(len(nums) - 2):
        if left > 0 and nums[left] == nums[left - 1]:
            continue

        mid = left + 1
        right = len(nums) - 1

        while mid < right:
            curr = nums[left] + nums[mid] + nums[right]
            if curr < 0:
                mid += 1
            elif curr > 0:
                right -= 1
            else:
                ret.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]:
                    mid += 1
                while mid < right and nums[right] == nums[right - 1]:
                    right -= 1
                mid += 1
                right -= 1
    return ret


# max area
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        max_area = max(max_area, (right - left) * min(height[right], height[left]))

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area

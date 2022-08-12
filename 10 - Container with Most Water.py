
#2 pointers compare left and right height and inch em together
def maxArea(height):
    left = 0
    right = len(height)- 1
    area = 0


    while left < right:

        area = max (area, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        

    return area


print(maxArea([1,8,6,2,5,4,8,3,7]))
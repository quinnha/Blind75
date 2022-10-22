def findKthLargest(nums, k):
        if nums == []: return 0

        return sorted(nums)[-k]
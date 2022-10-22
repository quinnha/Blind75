# neat math, if the set is not the same size of the list, then theres duplicates
# its because sets are unique!

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))
        
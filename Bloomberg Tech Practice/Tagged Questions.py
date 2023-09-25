# Insert Delete GetRandom O(1)
class RandomizedSet:
    def __init__(self):
        self.nums, self.position = [], {}

    def insert(self, val: int) -> bool:
        if val in self.position:
            return False
        self.nums.append(val)
        self.position[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.position:
            return False
        idx, last = self.position[val], self.nums[-1]
        self.nums[idx], self.position[last] = last, idx
        self.nums.pop()
        self.position.pop(val, 0)
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]

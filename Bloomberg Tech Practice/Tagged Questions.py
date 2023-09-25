import random
from collections import Counter


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


# Design underground system
class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        self.freqs = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, start_t = self.ids.pop(id)
        self.pairs[name, stationName] += t - start_t
        self.freqs[name, stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (
            self.pairs[startStation, endStation] / self.freqs[startStation, endStation]
        )

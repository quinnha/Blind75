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


# Decode String
def decodeString(s):
    stack = []
    currNum = 0
    currString = ""

    for c in s:
        if c == "[":
            stack.append(currString)
            stack.append(currNum)
            currNum = 0
            currString = ""

        elif c == "]":
            num = stack.pop()
            prevString = stack.pop()

            currString = prevString + num * currString

        elif c.isdigit():
            currNum = currNum * 10 + int(c)

        else:
            currString += c

    return currString


# number of islands (again lol)
def numIslands(grid):
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return

        grid[i][j] = "#"

        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    ret = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                ret += 1

    return ret


# two city scheduling
def twoCitySchedCost(costs):
    first = [i for i, j in costs]
    diff = sorted([j - i for i, j in costs])
    print(diff)
    return sum(first) + sum(diff[: len(costs) // 2])


# remove adjacent duplicates in string 2
def removeDuplicates(self, s: str, k: int) -> str:
    s = list(s)
    stack = [" "]

    for c in s:
        curr_string = stack.pop()

        if c == curr_string[-1]:
            curr_string += c
            if len(curr_string) != k:
                stack.append(curr_string)

        else:
            stack.append(curr_string)
            stack.append(c)

        if len(stack) == 0:
            stack.append(" ")

    stack = stack[1:]

    return "".join(x for x in stack)


# merge intervals
def merge(intervals):
    sort = sorted(intervals)
    out = []

    new_interval = sort[0]
    for interval in sort:
        if interval[0] <= new_interval[1]:
            new_interval[1] = max(new_interval[1], interval[1])
        else:
            out.append(new_interval)
            new_interval = interval

    return out + [new_interval]


# flatten multilevel doubly linked list
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head):
    # if child -> go into child
    # if next -> go into next
    # if none -> go all the way way

    if not head:
        return

    curr = Node()
    ret_head = curr
    stack = [head]
    prev = None

    while stack:
        node = stack.pop(-1)
        if not node:
            continue
        node.prev = prev
        prev = node
        curr.next = node
        curr = curr.next
        if node.next:
            stack.append(node.next)
        if node.child:
            stack.append(node.child)

    temp = ret_head.next
    prev = None

    # while temp:
    #     temp.prev = prev
    #     prev = temp
    #     temp = temp.next

    # while ret_head:
    #     print(ret_head.val, ret_head.prev, ret_head.next, ret_head.child)
    #     ret_head = ret_head.next
    return ret_head.next

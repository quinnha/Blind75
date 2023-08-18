# Day 5, Aug 17, https://leetcode.com/problems/maximal-network-rank/

from collections import defaultdict


def maximalNetworkRank(n, roads):
    ret = 0
    if n == 1:
        return 0

    d = defaultdict(set)

    for road in roads:
        d[road[0]].add(road[1])
        d[road[1]].add(road[0])

    for i in range(n):
        for j in range(i + 1, n):
            curr = len(d[i]) + len(d[j])
            if j in d[i]:
                curr -= 1
            print(i, j, curr)
            ret = max(ret, curr)

    return ret


print(maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
print(maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))

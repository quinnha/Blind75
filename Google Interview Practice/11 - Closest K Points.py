import heapq
def kClosest(points, k: int):
        
    return heapq.nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)

def kClosest2(points, k: int):
        
    return sorted(points, key = lambda x: x[0] ** 2 + x[1] ** 2)[:k]

print(kClosest2([[3,3],[5,-1],[-2,4]], 2))
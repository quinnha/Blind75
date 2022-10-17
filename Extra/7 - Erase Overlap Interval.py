
def eraseOverlapIntervals(intervals):

    sort = sorted(intervals, key = lambda x:x[0])
    counter = 0
    end = intervals[0][1]
    for interval in intervals:
        if interval[1] >= end: 
            end = interval[1] 
            counter += 1
    return len(intervals) - counter 

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

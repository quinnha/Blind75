# reverse sort and add one by one, greedy algo
def maximumUnits(boxTypes, truckSize):

    boxTypes.sort(key=lambda x: -x[1])
    boxes = 0

    for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else: # acts as if trucksize == box (will take largest)
                boxes += truckSize * units
                return boxes
    return boxes

boxTypes = [[1,3],[2,2],[3,1]]
boxTypes = [[5,10],[2,5],[4,7],[3,9]]

print(maximumUnits(boxTypes, 10))



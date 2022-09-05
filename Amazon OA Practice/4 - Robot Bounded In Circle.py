
def isRobotBounded(instructions):
    dx = 0
    dy = 1
    x = 0
    y = 0

    for instruction in instructions:
        if instruction == "L": 
            if dx != 0: dx, dy = dy, dx 
            else: dx, dy, = -dy, -dx 
        elif instruction == "R":
            if dx != 0: dx, dy = -dy, -dx 
            else: dx, dy, = dy, dx 
        else: 
            if dx == 1: x +=1
            elif dx == -1: x -= 1
            elif dy == 1: y += 1
            elif dy == -1: y -= 1
    
    return (x, y) == (0,0) or (dx, dy) != (0,1)


print(isRobotBounded("GL"))
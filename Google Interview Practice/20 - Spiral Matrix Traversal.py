# Untested, this was whiteboarding
def traverse(grid):
        horizontal = len(grid[0])
        vertical = len(grid)
        direction = ["R", "D", "L", "U"]
        counter = 0

        column1 = 0
        column2 = len(grid[0]) - 1
        row1 = 0
        row2 = len(grid) - 1

        current_row = 0
        current_col = len(grid[0]) - 1

        while horizontal != 0 and vertical != 0:
            cur_direction = direction[counter % 4]
            if cur_direction == "R":
                for i in range(column1, column2 + 1):
                    print(grid[row1][i])
                horizontal -= 1
                row1 += 1
            elif cur_direction == "L":
                for i in range(column2, column1 + 1):
                    print(grid[row2][i])
                horizontal -= 1
                row2 -= 1
            elif cur_direction == "D":
                for i in range(row1, row2 + 1):
                    print(grid[i][column2])
                vertical -= 1
                column2 -= 1
            elif cur_direction == "U":
                for i in range(column1, column2 + 1):
                    print(grid[i][column1])
                vertical -= 1
                row1 += 1

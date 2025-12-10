numRolls = 0
grid = []
xLen = 137
yLen = 137
grid2 = []
row = []

for i in range(0, 138):
    for j in range(0,138):
        row.append("")
    grid2.append(row)
    row = []


"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.


..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""





with open("Misc/Day4/Day4.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            if grid[row][col] == "@":
                #print(x, y)  
                count = 0  
                if col > 0:
                    if grid[row][col-1] == "@":
                        count += 1
                    if row > 0:
                        if grid[row-1][col-1] == "@":
                            count += 1
                    if row < yLen:
                        if grid[row+1][col-1] == "@":
                            count += 1
                
                if col < xLen:
                    if grid[row][col+1] == "@":
                        count += 1

                    if row > 0:
                        if grid[row-1][col+1] == "@":
                            count += 1
                    if row < yLen:
                        if grid[row+1][col+1] == "@":
                            count += 1

                if row > 0:
                    if grid[row-1][col] == "@":
                        count += 1

                if row < yLen:
                    if grid[row+1][col] == "@":
                        count += 1
                
                if count < 4:
                    grid2[row][col] = "x"
                    numRolls += 1
                
                else:
                    grid2[row][col] = grid[row][col]
                    
            else:
                grid2[row][col] = grid[row][col]

    print(numRolls)
    #for row in grid2:
    #    print(row)
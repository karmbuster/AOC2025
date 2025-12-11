totalNumRolls = 0
xLen = 137
yLen = 137
rollGrid = []




def removeRolls(grid):
    numRolls = 0
    grid2 = []
    row = []

    for i in range(0, 138):
        for j in range(0,138):
            row.append("")
        grid2.append(row)
        row = []


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
                    grid2[row][col] = "."
                    numRolls += 1
                
                else:
                    grid2[row][col] = grid[row][col]
                    
            else:
                grid2[row][col] = grid[row][col]

    return grid2, numRolls


with open("Misc/Day4/Day4.txt", "r") as f:
    for line in f:
        rollGrid.append(list(line.strip()))
    
    currentRolls = -1

    while currentRolls != 0:
        rollGrid, currentRolls = removeRolls(rollGrid)
        totalNumRolls = totalNumRolls + currentRolls
    
    print(totalNumRolls)


    



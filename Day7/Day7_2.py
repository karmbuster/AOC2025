import re

puzzleInList = []
sum = 0


with open("Misc/Day7/Day7.txt", "r") as f:

    for line in f:
        
        line = line.strip()
        tempList = []
        for char in line:
            tempList.append(char)
        puzzleInList.append(tempList)

    
    for i in range(0, len(puzzleInList)):
        
        if i == 0:
            tempIndex = puzzleInList[i].index("S")
            puzzleInList[i][tempIndex] = '1'
        
        else:
            if puzzleInList[i].count("^") == 0:
                puzzleInList[i] = puzzleInList[i-1]
                for a in range(0,len(puzzleInList[i])):
                    if puzzleInList[i][a] == "^":
                        puzzleInList[i][a] = "."
            
            else:
                indexes = [j for j, x in enumerate(puzzleInList[i]) if x == "^"]

                for index in indexes:

                    if puzzleInList[i-1][index].isdigit(): # if the row above has a number where the ^ is on the current line
                        if puzzleInList[i][index-1].isdigit():
                            puzzleInList[i][index-1] = str(int(puzzleInList[i][index-1]) + int(puzzleInList[i-1][index]))
                        else:
                            puzzleInList[i][index-1] = puzzleInList[i-1][index]
                        if puzzleInList[i][index+1].isdigit():
                            puzzleInList[i][index+1] = str(int(puzzleInList[i][index+1]) + int(puzzleInList[i-1][index]))
                        else:
                            puzzleInList[i][index+1] = puzzleInList[i-1][index]
                        
                
                for j in range(0, len(puzzleInList[i])):
                    if j not in indexes:
                        if puzzleInList[i-1][j].isdigit():
                            if puzzleInList[i][j].isdigit():
                                puzzleInList[i][j] = str(int(puzzleInList[i][j]) + int(puzzleInList[i-1][j]))
                            else:
                                puzzleInList[i][j] = puzzleInList[i-1][j]
        
        if i == (len(puzzleInList)-1):
            for j in range(0, len(puzzleInList[i])):
                if puzzleInList[i][j].isdigit():
                    sum = sum + int(puzzleInList[i][j])
    
    print(sum)
                




            
import re

firstLine  = 1
indexList = []
totalSplits = 0



with open("Misc/Day7/Day7.txt", "r") as f:

    for line in f:
        #print(indexList)
        if firstLine == 1:
            indexList.append(line.find("S"))
            firstLine = 0
            #print(indexList)

        if line.find("^") == -1:
            pass

        else:
            tempList = []
            for x in range(0, len(indexList)):
                if line[indexList[x]] == "^":
                    
                    tempList.append(indexList[x]-1)
                    tempList.append(indexList[x]+1)

                    #indexList.remove(x)
                    totalSplits += 1
                else:
                    tempList.append(indexList[x])
            
            indexList = []
            for y in tempList:
                if y not in indexList: indexList.append(y)

print(totalSplits)

                    





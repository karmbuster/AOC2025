
finalSet = set()
totalFresh = 0

"""
with open("Misc/Day5/Day5_Range.txt", "r") as f:
   
    for fline in f:
        tempList = []
        startIndex = int(fline.strip().split('-')[0])
        endIndex = int(fline.strip().split('-')[1])

        for i in range(startIndex, endIndex + 1):
            tempList.append(i)
        
        finalSet = finalSet.union(set(tempList))

print(len(finalSet))
"""

rangeList = []

with open("Misc/Day5/Day5_Range.txt", "r") as f:

    for line in f:
        #tempList = []
        startIndex = int(line.strip().split('-')[0])
        endIndex = int(line.strip().split('-')[1])

        rangeList.append((startIndex, endIndex))
    
    rangeList.sort()
    #print(rangeList)

    for i in range(0, len(rangeList)):

        if i == 0:
            totalFresh = totalFresh + (rangeList[i][1] - rangeList[i][0]) + 1
        
        else:
            if rangeList[i][0] > rangeList[i-1][1]:
                totalFresh = totalFresh + (rangeList[i][1] - rangeList[i][0] + 1)
            
            elif rangeList[i][0] <= rangeList[i-1][1]:
               
                if rangeList[i][1] <= rangeList[i-1][1]:
                    rangeList[i] = (rangeList[i-1])
               
                else:
                    tLength = rangeList[i][1] - rangeList[i-1][1]
                
                    totalFresh = totalFresh + tLength
               
    print(totalFresh)
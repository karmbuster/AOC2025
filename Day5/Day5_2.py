
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
    print(rangeList)

    for i in range(0, len(rangeList)):

        #print(rangeList[i])

        if i == 0:
            totalFresh = totalFresh + (rangeList[i][1] - rangeList[i][0]) + 1
            #print(rangeList[i][1], rangeList[i][0], totalFresh)
        
        else:

       
            if rangeList[i][0] > rangeList[i-1][1]:
             
                #current = 10-14
                #previous = 3-5
                #10-14 is completely outside of 3-5 so add all ingredients in this next list
            
                # if first number of range is greater than the last number of previous range, then do nothing as this and all future ranges 
                # have to be outside and greater of the range before
                totalFresh = totalFresh + (rangeList[i][1] - rangeList[i][0] + 1)
                #print(rangeList[i][1], rangeList[i][0], totalFresh)

            

            elif rangeList[i][0] <= rangeList[i-1][1]:
                #"""
                #current = 16-20
                #previous = 12-16 or previous 
                #"""
                # 12 - 16
                # 12 - 17
                # tLength = 20 - 16 = 4 - we should already be including 16, so just add 4 

                if rangeList[i][1] <= rangeList[i-1][1]:
                    rangeList[i] = (rangeList[i-1])
                    #rangeList[i][1] = rangeList[i-1][1]

                else:
                    tLength = rangeList[i][1] - rangeList[i-1][1]
                
                    totalFresh = totalFresh + tLength
                    #print(rangeList[i][1], rangeList[i-1][1], totalFresh)

    print(totalFresh)
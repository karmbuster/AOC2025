import math

boxList = []
index = 0
distDict = {}

def calculateDistance(l1, l2):

    tempCalcList = []
    tempCalcSum = 0

    for i in range(0, len(l1)):
        tempCalcList.append((l1[i]-l2[i]) * (l1[i] - l2[i]))
    
    for j in range(0, len(tempCalcList)):
        tempCalcSum = tempCalcSum + tempCalcList[j]

    return math.sqrt(tempCalcSum)

with open("Misc/Day8/Day8.txt", "r") as f:

    for line in f:
        tempList = line.strip().split(',')
        for i in range(0, len(tempList)):
            tempList[i] = int(tempList[i])
        boxList.append(tempList)

    # calculcate distances
    for i in range(0, len(boxList) - 1):
        for j in range(i + 1, len(boxList)):
            difference = calculateDistance(boxList[i], boxList[j])
            tempTuple = (i, j)
            distDict[tempTuple] = difference
    
    sortedDistDict = {k:v for k,v in sorted(distDict.items(), key=lambda item: item[1])}


with open("Misc/Day8/Day8_w_practice.txt", "w") as file:
    for key, value in sortedDistDict.items():
        file.write(str(key[0]) + "," + str(key[1]) + "," + str(value) + "\n")
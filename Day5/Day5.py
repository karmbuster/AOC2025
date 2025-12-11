rangesList = []
ingList = []
numFresh = 0

with open("Misc/Day5/Day5_Range.txt", "r") as f:
   
    for fline in f:
        tempTuple = (int(fline.strip().split("-")[0]), int(fline.strip().split("-")[1]))
        rangesList.append(tempTuple)
    

with open("Misc/Day5/Day5_Ing.txt", "r") as g:

    for gline in g:
        ingList.append(int(gline.strip()))

for i in ingList:
    for j in rangesList:
        if j[0] <= i <= j[1]:
            numFresh += 1
            break

print(numFresh)

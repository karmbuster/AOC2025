opList = []
numList = []
sum = 0

with open("Misc/Day6/Day6_oper.txt", "r") as opFile:
    opList = list(opFile.readline().strip().replace(" ", ""))

with open("Misc/Day6/Day6_num.txt", "r") as numFile:
    for line in numFile:
        tempList = [int(x) for x in line.split() if x.isdigit()]
        numList.append(tempList)

for o in range(0, len(opList)):
    
    if opList[o] == "*":
        result = 1
    else:
        result = 0

    for i in range(0, len(numList)):
        if opList[o] == "*":
            result = result * numList[i][o]

        else:
            result = result + numList[i][o]

    sum = sum + result

print(sum)            
            
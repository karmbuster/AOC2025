lineList = []
operIndex = 0
sum = 0

with open("Misc/Day6/Day6_oper.txt", "r") as opFile:
    opList = list(opFile.readline().strip().replace(" ", ""))


with open("Misc/Day6/Day6_num.txt", "r") as numFile:
    for line in numFile:
        lineList.append(line.strip("\n"))

def calcTotal(l, ind):
    
    if opList[ind] == "*":
        tempSum = 1
        for i in l:
            tempSum = tempSum * int(i)

    else:
        tempSum = 0
        for i in l:
            tempSum = tempSum + int(i)
    
    return tempSum

numList = []

print(lineList[0])

for i in range(0, len(lineList[0])):

    if (lineList[0][i] == lineList[1][i] == lineList[2][i] == lineList[3][i] == " "):
        
        sum = sum + calcTotal(numList, operIndex)
        operIndex += 1
        numList = []

    else:
        numList.append(lineList[0][i] + lineList[1][i] + lineList[2][i] + lineList[3][i])

        if i == len(lineList[0]) - 1:
            sum = sum + calcTotal(numList, operIndex)

print(sum)
    
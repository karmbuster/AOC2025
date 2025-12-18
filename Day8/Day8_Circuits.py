Practice = False

calcList = []
circuitList = [] # each circuit is a list and this circuit list is a list that holds all the circuits.  

if Practice:
    with open("Day8/Day8_w_practice.txt", "r") as f:
        for line in f:
            calcList.append(line.strip())

else:
    with open("Day8/Day8_w_actual.txt", "r") as f:
        for line in f:
            calcList.append(line.strip())

index = 0

for x in calcList:
    #if index < 1000: # Remove for part 2
        tempList = x.split(",")
        index1 = -1
        index2 = -1
        tempCircList = []
    
        for y in range(0, len(circuitList)):
            for z in range(0, len(circuitList[y])):
                if tempList[0] == circuitList[y][z]:
                    index1 = y
        
        for y in range(0, len(circuitList)):
            for z in range(0, len(circuitList[y])):
                if tempList[1] == circuitList[y][z]:
                    index2 = y
        
        if index1 == index2 == -1:
            # neither is in a circuit list already - add new circuit list with the two indeces.
            tempCircList.append(tempList[0])
            tempCircList.append(tempList[1])
            circuitList.append(tempCircList)
        
        elif index1 == index2 != -1:
            # both are in the same circuit list - do nothing as they are already handled - not sure if this could even happen
            #print("not sure this should ever happen")
            pass
            
        elif index1 == -1 and index2 != -1:
            circuitList[index2].append(tempList[0])
            if len(circuitList[index2]) == 1000: # Add for Part 2
                print(tempList[0], tempList[1]) # Add for Part 2
        
        elif index1 != -1 and index2 == -1:
            circuitList[index1].append(tempList[1])
            if len(circuitList[index1]) == 1000: # Add for Part 2
                print(tempList[0], tempList[1]) # Add for Part 2

        elif index1 != -1 and index2 != -1 and index1 != index2:
            # both are found in different circuits - combine the circuits?
            tList1 = circuitList[index1]
            tList2 = circuitList[index2]
            tempCombinedList = circuitList[index1] + circuitList[index2]
            circuitList.remove(tList1)
            circuitList.remove(tList2)
            circuitList.append(tempCombinedList)
            #print(tempCombinedList)
            if len(tempCombinedList) == 1000: # Add for Part 2
                print(tempList[0], tempList[1]) # Add for Part 2
        #index = index + 1 # Remove for Part 1

#print(circuitList)

#circuitList.sort(key=len, reverse=True) # Remove for Part 1

#print(len(circuitList[0]) * len(circuitList[1]) * len(circuitList[2])) # Remove for Part 1

#print(circuitList)


# Part 2 results
#364 515 are the indexes for the last two circuits before the circuit becomes 1 circuit

# 68306,16270,43777 - looking at the circuit list, this is the circuit at index 364 (line 365 in the text file)
# 71516,2598,44649 - looking at the circuit list, this is the circuit at index 515 (line 516 in the text file)

# answer = 68306 * 71516 = 4,884,971,896 - multiple the x values to get the answer.


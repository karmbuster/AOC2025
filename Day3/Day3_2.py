sum = 0

def findGreatestDigitandPos(s):
    tempList = []
    for char in s:
        tempList.append(int(char))
    
    return max(tempList), tempList.index(max(tempList))


with open("Misc/Day3/Day3.txt", "r") as f:
    for line in f:

        numToRemove = 88
        index = 0
        joltageValue = ''
        numString = line.strip()

        #print(numString)
        
        while len(joltageValue) < 12:

            if index > len(numString) - 1:
                print("something went wrong")
            
            if numToRemove > 0:
                subStr = numString[index:(index + numToRemove + 1)]
                maxValue, maxValuePos = findGreatestDigitandPos(subStr)

                numToRemove = numToRemove - maxValuePos
                index = index + maxValuePos + 1
                joltageValue = joltageValue + str(maxValue)

            else:
                joltageValue = joltageValue + numString[index]
                index = index + 1
        #print(joltageValue) 
        sum = sum + int(joltageValue)

    print(sum)

        
        
            



            

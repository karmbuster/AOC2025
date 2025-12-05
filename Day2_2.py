import re

sum = 0

with open("Day2.txt", "r") as f:

    rangeList = f.readline().split(",")
    for IDRange in rangeList:
        firstID = int(IDRange.split("-")[0])
        lastID = int(IDRange.split("-")[1])

        for i in range(firstID, lastID + 1):

            # see how many digits the number is.
            digits = len(str(i))
            # half of the number of digits is the max number of digits a match can be.
            halfDigits = int(digits / 2)

            if digits > 1:
                for j in range(1, halfDigits + 1):
                    # Check for numbers divisible by number of digits
                    # to see the valid number of digits for patterns
                    # half is the max the number can be to have a repeat
                    if digits % j == 0:
                        patternToCheck = str(i)[:j]
                        matches = re.findall(patternToCheck, str(i))
                        if len(matches) == digits / j:
                            # print(i)
                            sum = sum + i
                            break
    print(sum)

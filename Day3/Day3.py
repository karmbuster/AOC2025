sum = 0

with open("Misc/Day3/Day3.txt", "r") as f:
    # Comment: Day1.txt
    for line in f:
        firstDigit = -1
        secondDigit = -1
        firstDigitIndex = -1
        secondDigitIndex = -1
        flipNumbers = False

        bank = line.strip()
        for i in range(9, 0, -1): # i is int
            for j in range(0, len(list(bank))):
                if i == int(list(bank)[j]) and firstDigit == -1 and firstDigitIndex == -1:
                    firstDigit = i
                    firstDigitIndex = j
        #print(firstDigit, firstDigitIndex)
        
        if firstDigitIndex != len(list(bank))-1:
            for k in range(9, 0, -1):
                for l in range(firstDigitIndex + 1, len(list(bank))):
                    if k == int(list(bank)[l]) and secondDigit == -1 and secondDigitIndex == -1:
                       secondDigit = k
                       secondDigitIndex = l
        else:
            for m in range(9, 0, -1):
                for n in range(0, len(list(bank)) - 1):
                    if m == int(list(bank)[n]) and secondDigit == -1 and secondDigitIndex == -1:
                        secondDigit = m
                        secondDigitIndex = n
                        flipNumbers = True
        
        if flipNumbers:
            sum = sum + int(str(secondDigit) + str(firstDigit))
        
        else:
            sum = sum + int(str(firstDigit) + str(secondDigit))


        
        
        #print(secondDigit, secondDigitIndex)
    print(sum)
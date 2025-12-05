sum = 0

with open("Misc/Day2.txt", "r") as f:
    
    rangeList = f.readline().split(",")
    for IDRange in rangeList:
        firstID = int(IDRange.split('-')[0])
        lastID = int(IDRange.split('-')[1])

        for i in range(firstID, lastID + 1):
            # make sure there are an even number of digits
            if len(str(i)) % 2 == 0:
                # get halfway point of the length of the ID
                IDLengthby2 = int(len(str(i))/2)
                # split into first half and second half
                IDFirstHalf = int(str(i)[:IDLengthby2])
                IDSecondHalf = int(str(i)[IDLengthby2:])

                if IDFirstHalf == IDSecondHalf:
                    sum = sum + i
            else:
                # do nothing because there is an odd number of digits
                pass
    
    print(sum)














       







                
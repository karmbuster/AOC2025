count = 0
dial = 50

with open("Day1.txt", "r") as f:
    for line in f:
        # print(line)
        turns = int(line.strip()[1:])
        # print(turns)

        print(dial)
        print(line)

        if line[0] == "L":
            if turns > 99:
                extra = int(str(turns)[0])
                count = count + extra
                turns = int(str(turns)[-2:])
            if turns > dial:
                startDial = dial
                overflow = turns - dial
                dial = 100 - overflow
                if (dial != 0) and (startDial != 0):
                    count += 1
                    print("turn left through 0")
            else:
                dial = dial - turns
            if dial == 0:
                count += 1

        elif line[0] == "R":
            if turns > 99:
                extra = int(str(turns)[0])
                count = count + extra
                turns = int(str(turns)[-2:])
            if (turns + dial) > 99:
                startDial = dial
                overflow = turns - (99 - dial)
                dial = -1 + overflow
                if (dial != 0) and (startDial != 0):
                    count += 1
                    print("turn right  through 0")
            else:
                dial = dial + turns
            if dial == 0:
                count += 1

        else:
            print("Something went wrong")

    print(count)

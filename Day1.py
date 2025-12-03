count = 0
dial = 50

with open("Day1.txt", "r") as f:
    for line in f:
        # print(line)
        turns = int(line.strip()[1:])
        # print(turns)

        if turns > 99:
            turns = int(str(turns)[-2:])

        # print(turns)

        # print(dial)
        # print(line)

        if line[0] == "L":
            if turns > dial:
                # dial = 50, turns = 68
                overflow = turns - dial  # overflow = 18
                dial = 100 - overflow
                # if dial != 0:
                #    count += 1
                #    print("turn left through 0")
            else:
                dial = dial - turns
            if dial == 0:
                count += 1

        elif line[0] == "R":
            if (turns + dial) > 99:
                overflow = turns - (99 - dial)
                dial = -1 + overflow
                # if dial != 0:
                #    count += 1
                #    print("turn right  through 0")
            else:
                dial = dial + turns
            if dial == 0:
                count += 1

        else:
            print("Something went wrong")

    print(count)

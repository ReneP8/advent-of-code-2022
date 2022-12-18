file = open("input.txt", "r")

# reading lines from text file
lines = file.readlines()


def ranges_fully_contained():
    fully_contained = 0
    for line in lines:
        sections = line.strip("\n").split(',')

        range1 = range(int(sections[0].split('-')[0]),
                       int(sections[0].split('-')[1])+1)
        range2 = range(int(sections[1].split('-')[0]),
                       int(sections[1].split('-')[1])+1)

        if range1.start in range2 and range1.stop-1 in range2:
            fully_contained += 1
        elif range2.start in range1 and range2.stop-1 in range1:
            fully_contained += 1

    print(fully_contained)


def ranges_overlap():
    overlapping = 0

    for line in lines:
        sections = line.strip("\n").split(',')

        range1 = range(int(sections[0].split('-')[0]),
                       int(sections[0].split('-')[1])+1)
        range2 = range(int(sections[1].split('-')[0]),
                       int(sections[1].split('-')[1])+1)

        if (range1.start <= range2.stop-1) and (range1.stop-1 >= range2.start):
            overlapping += 1

    print(overlapping)

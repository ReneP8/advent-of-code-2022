one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

lists = [one, two, three, four, five, six, seven, eight, nine]

with open("input.txt", "r") as file:
    lines = file.readlines()[:8]
    for line in lines:
        one.append(line[1])
        two.append(line[5])
        three.append(line[9])
        four.append(line[13])
        five.append(line[17])
        six.append(line[21])
        seven.append(line[25])
        eight.append(line[29])
        nine.append(line[33])

    for lst in lists:
        lst.reverse()

print(lists)

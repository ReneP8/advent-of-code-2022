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

file = open("input.txt", "r")

# reading lines from text file
lines = file.readlines()


def prepare_stacks():
    picture_of_crates = lines[:8]
    for line in picture_of_crates:
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
        while ' ' in lst:
            lst.remove(' ')

    print(lists)


def move_crates():
    for line in lines[10:]:
        line = line.strip('\n')

        values = line.split(' ')
        values.remove('move')
        values.remove('from')
        values.remove('to')

        for i in range(int(values[0])):
            removing = lists[int(values[1])-1].pop()
            lists[int(values[2])-1].append(removing)

    result = ''
    for list in lists:
        result += list[-1]

    print(result)


if __name__ == '__main__':
    prepare_stacks()
    move_crates()

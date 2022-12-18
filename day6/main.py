file = open("input.txt", "r")

# reading lines from text file
line = file.readline()


def part_one():
    found_index = -1
    for index in range(len(line) - 3):
        substring = line[index:index+4]
        # Check if the substring has four unique characters
        if len(set(substring)) == 4:
            if found_index == -1:
                found_index = index+4

    print(found_index)


def part_two():
    found_index = -1
    for index in range(len(line) - 13):
        substring = line[index:index+14]
        # Check if the substring has four unique characters
        if len(set(substring)) == 14:
            if found_index == -1:
                found_index = index+14

    print(found_index)


part_two()

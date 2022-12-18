file = open("input.txt", "r")

# reading lines from text file
line = file.readline()

found_index = -1
for index in range(len(line) - 3):
    substring = line[index:index+4]
    # Check if the substring has four unique characters
    if len(set(substring)) == 4:
        if found_index == -1:
            found_index = index+4

print(found_index)

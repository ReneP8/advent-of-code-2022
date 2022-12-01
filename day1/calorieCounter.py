file = open("input.txt", "r")

# reading lines from text file
lines = file.readlines()

# list for total calories
totalCals = []
calSum = 0
for line in lines:
    line = line.strip("\n")
    if len(line) == 0:
        totalCals.append(calSum)
        calSum = 0
    else:
        calSum += int(line)

# sorting by number
totalCals.sort()
print(totalCals.pop())

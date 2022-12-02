# read line by line
# get value for choosen piece (rock=1, paper=2, scissors=3)
# get value for outcome
# sum up both values
# calculate total sum by adding sum

file = open("input.txt", "r")

# reading lines from text file
lines = file.readlines()


def part_one():
    totalScore = 0
    for line in lines:
        figure_score = 0
        outcome_score = 0
        line = line.strip("\n").split()

        opponent = line[0]
        me = line[1]

        if me == "X":
            figure_score = 1
        elif me == "Y":
            figure_score = 2
        elif me == "Z":
            figure_score = 3

        if opponent == "A" and me == "X":
            outcome_score = 3
        elif opponent == "A" and me == "Y":
            outcome_score = 6
        elif opponent == "A" and me == "Z":
            outcome_score = 0

        if opponent == "B" and me == "X":
            outcome_score = 0
        elif opponent == "B" and me == "Y":
            outcome_score = 3
        elif opponent == "B" and me == "Z":
            outcome_score = 6

        if opponent == "C" and me == "X":
            outcome_score = 6
        elif opponent == "C" and me == "Y":
            outcome_score = 0
        elif opponent == "C" and me == "Z":
            outcome_score = 3

        totalScore += figure_score + outcome_score

    print("Your total score would be: " + str(totalScore))


def part_two():
    totalScore = 0
    for line in lines:
        figure_score = 0
        outcome_score = 0
        line = line.strip("\n").split()

        opponent = line[0]
        me = line[1]

        if opponent == "A" and me == "X":
            figure_score = 3
            outcome_score = 0
        elif opponent == "A" and me == "Y":
            figure_score = 1
            outcome_score = 3
        elif opponent == "A" and me == "Z":
            figure_score = 2
            outcome_score = 6

        if opponent == "B" and me == "X":
            figure_score = 1
            outcome_score = 0
        elif opponent == "B" and me == "Y":
            figure_score = 2
            outcome_score = 3
        elif opponent == "B" and me == "Z":
            figure_score = 3
            outcome_score = 6

        if opponent == "C" and me == "X":
            figure_score = 2
            outcome_score = 0
        elif opponent == "C" and me == "Y":
            figure_score = 3
            outcome_score = 3
        elif opponent == "C" and me == "Z":
            figure_score = 1
            outcome_score = 6

        totalScore += figure_score + outcome_score

    print("2. Your total score would be: " + str(totalScore))


part_one()
part_two()

with open("puzzle_input_2.txt", "r") as file:
    lines = file.read().splitlines()
    total_score = []
    for line in lines:
        opponent = line[0]
        me = line[2]
        if me == "X":
            score = 1
            if opponent == "A":
                score = score + 3
            elif opponent == "B":
                score = score + 0
            else:
                score = score + 6
        elif me == "Y":
            score = 2
            if opponent == "A":
                score = score + 6
            elif opponent == "B":
                score = score + 3
            else:
                score = score + 0
        else:
            score = 3
            if opponent == "A":
                score = score + 0
            elif opponent == "B":
                score = score + 6
            else:
                score = score + 3
        total_score.append(score)
    print(f"total_score: {sum(total_score)}")

print("-----------------------")

with open("puzzle_input_2.txt", "r") as file:
    lines = file.read().splitlines()
    total_score = []
    for line in lines:
        opponent = line[0]
        me = line[2]
        if me == "X":  # lose
            score = 0
            if opponent == "A":  # rock
                score = score + 3
            elif opponent == "B":  # paper
                score = score + 1
            else:  # scissors
                score = score + 2
        elif me == "Y":  # draw
            score = 3
            if opponent == "A":  # rock
                score = score + 1
            elif opponent == "B":  # paper
                score = score + 2
            else:  # scissors
                score = score + 3
        else:  # win
            score = 6
            if opponent == "A":  # rock
                score = score + 2
            elif opponent == "B":  # paper
                score = score + 3
            else:  # scissors
                score = score + 1
        total_score.append(score)
    print(f"new_total_score: {sum(total_score)}")

"""
A = Rock
B = Paper
C = Scissors
X = Lose + 0
Y = Draw + 3
Z = Win + 6
"""
with open("puzzle_input_5.txt", "r") as file:
    line_list = file.read().splitlines()

# Part I
# Crates
crates_dict = {}
crates_list = []
crate = []

for j in range(0, 32, 4):
    for i in reversed(range(8)):
        item = line_list[i][(j):(j + 3)]
        if item != "   ":
            crate.append(item)
    crates_list.append(crate)
    crate = []

print(crates_list)
#print(crates_dict)

stacks = line_list[8].split()
print(stacks)

for i in range(9):
    crates_dict = dict(stacks[i], crates_list[i])


# Instructions
instructions_line = list(line_list[10:])
remove_set = ["move", "from", "to"]
instructions_list = [instruction.split() for instruction in instructions_line]

for instruction in instructions_list:
    for char in instruction:
        if char in remove_set:
            instruction.remove(char)

print(instructions_list)  # instruction = [amount to move, current stack, new stack]
#print(instruction_details)
#print(instructions)
#print(len(instructions))

# Part II
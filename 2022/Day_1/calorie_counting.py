with open("puzzle_input_1.txt", "r") as file:
    lines_list = file.read().splitlines()
    lines_list = [int(food) if bool(food) != False else food for food in lines_list]

# Part I
total_calories = []
elf_calories =[]

for calories in lines_list:
    if calories != "":
        elf_calories.append(calories)
    else:
        total_calories.append(elf_calories)
        elf_calories = []
        continue

total_calories_sum = [sum(elf) for elf in total_calories]

print(f"The elf carrying the most calories is carrying: {max(total_calories_sum)} calories")

# Part II
total_calories_sum.sort(reverse=True)
calories_top3 = sum(total_calories_sum[0:3])

print(total_calories_sum)
print(f"The top 3 elves are carrying {calories_top3} calories total")

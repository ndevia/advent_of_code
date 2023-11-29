lowercase_types = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_types = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowercase_priorities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
uppercase_priorities = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

with open("puzzle_input_3.txt", "r") as file:
    lines = file.read().splitlines()
    total = []
    for word in lines:
        index = int(len(word) / 2)
        first_compartment = word[:index]
        second_compartment = word[index:]
        repeated_items = set([item for item in word if item in first_compartment and item in second_compartment])
        for i in range(26):
            repeated_items = [lowercase_priorities[i] if item == lowercase_types[i] else item for item in repeated_items]
            repeated_items = [uppercase_priorities[i] if item == uppercase_types[i] else item for item in repeated_items]
        rucksack_priority = sum(repeated_items)
        total.append(rucksack_priority)
    print(f"Total priorities: {sum(total)}")

print("-----------------------------")

with open("puzzle_input_3.txt", "r") as file:
    lines = file.read().splitlines()
    badges = []
    start = 0
    end = start + 3
    while start <=297 and end <= 300:
        elf_group = lines[start:end]
        group_badge = []
        for group in elf_group:
            badge_letter = [item for item in group if item in elf_group[0] and item in elf_group[1] and item in elf_group[2]]
            badge_letter_set = set(badge_letter)
            badge_letter = "".join(badge_letter_set)
            if badge_letter not in group_badge:
                group_badge.append(badge_letter)
                group_badge = "".join(group_badge)
        badges.append(group_badge)
        start = start + 3
        end = end + 3
    for i in range(26):
        badges = [lowercase_priorities[i] if item == lowercase_types[i] else item for item in badges]
        badges = [uppercase_priorities[i] if item == uppercase_types[i] else item for item in badges]
    badges_priorities = sum(badges)
    print(f"Elf group priorities: {badges_priorities}")
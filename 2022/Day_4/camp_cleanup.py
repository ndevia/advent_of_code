with open("puzzle_input_4.txt", "r") as file:
    lines = file.read().splitlines()
    contains = 0
    overlap = 0

    for line in lines:
        line = line
        pairs = line.split(",")

        elf1_index = pairs[0].split("-")
        start1 = int(elf1_index[0])
        end1 = int(elf1_index[1]) + 1

        elf2_index = pairs[1].split("-")
        start2 = int(elf2_index[0])
        end2 = int(elf2_index[1]) + 1

        first_elf = list(range(start1, end1))
        second_elf = list(range(start2, end2))

        if start1 in second_elf and (end1 - 1) in second_elf:
            contains += 1
        elif start2 in first_elf and (end2 - 1) in first_elf:
            contains += 1

        if start1 in second_elf or (end1 - 1) in second_elf:
            overlap += 1
        elif start2 in first_elf or (end2 - 1) in first_elf:
            overlap += 1

    print(f"fully_contain: {contains}")
    print("-------------------")
    print(f"overlap: {overlap}")
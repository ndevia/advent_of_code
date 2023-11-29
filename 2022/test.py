with open('puzzle_input_1.txt', 'r') as file:
    answer = {}
    elf_list = []
    for line in file:
        line = line.split()
        print(line)
        if not line:  # empty line?
            print(f"elf_{str(len(elf_list) + 1)}")
            elf_list.append("elf")
            continue
        answer[line[0]] = line[1:]
    print(answer)
    print(len(elf_list))
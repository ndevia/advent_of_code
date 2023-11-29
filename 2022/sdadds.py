x = open("puzzle_input_3.txt", "r").read().splitlines()

t = 0

from string import ascii_uppercase, ascii_lowercase

for i in x:
    a,b=i[:len(i)//2], i[len(i)//2:]

    for r in a:
        if r in b:
            if r.islower():t+=ascii_lowercase.index(r)+1
            else:t+=ascii_uppercase.index(r)+27
            break


print(t)



elf_list = []
    #laceholder_list = []p
lists_list = []

# List of Elves:
with open('puzzle_input_1.txt', 'r') as file:
    for line in file:
        if line == "\n":
            #print(f"elf_{str(len(elf_list) + 1)}")
            elf_list.append(f"elf_{str(len(elf_list) + 1)}")

# List of Calories:
with open('puzzle_input_1.txt', 'r') as file:
    calories_list = []
    for line in file:
        if line == "\n":
            break
        else:
            line = line.strip()
            calories_list.append(line)
            print(line)
        print(calories_list)
    lists_list.append(calories_list)


            #line.split()
            #placeholder_list = []
            #placeholder_list.append(line.strip())
            #print(line.strip())
    #print(placeholder_list)

        #if not line:  # empty line?
         #   print()
          #  elf_list.append(f"elf_{str(len(elf_list) + 1)}")
           # continue
        #else:
         #   lists_list.append(line)
          #  if not line:
           #     continue

print(elf_list)
print(len(elf_list))
print(lists_list)
    #print(len(lists_list))
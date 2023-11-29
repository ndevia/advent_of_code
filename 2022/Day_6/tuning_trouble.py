with open("puzzle_input_6.txt", "r") as file:
    text = file.read()

# Part I
text_list = list(text)
packet_counter = 1
message_counter = 1

for i in range(len(text_list) - 3):
    char_list = text_list[i:(i + 4)]
    char_set = set(char_list)
    if len(char_set) == 4:
        break
    packet_counter += 1
print(f"{packet_counter + 3} characters need to be processed before the first start-of-packet marker is detected")

for i in range(len(text_list) - 13):
    char_list = text_list[i:(i + 14)]
    char_set = set(char_list)
    if len(char_set) == 14:
        break
    message_counter += 1
print(f"{message_counter + 13} characters need to be processed before the first start-of-message marker is detected")
import string

with open("input_5.txt") as file:
    for line in file:
        line = line.replace("\n", "")


def len_after_reducing(line):
    while True:
        change = False
        for char in string.ascii_lowercase:
            if (char + char.upper() in line) or (char.upper() + char in line):
                change = True
                line = line.replace(char + char.upper(), "")
                line = line.replace(char.upper() + char, "")
        if not change:
            break
    return len(line)


print("PART 1")
print(len_after_reducing(line))
lengths = []
for char in string.ascii_lowercase:
    up = char.upper()
    length = len_after_reducing(line.replace(char, "").replace(up, ""))
    lengths.append(length)
print("PART 2")
print(min(lengths))

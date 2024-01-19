import re
from collections import Counter


def rotate(letter, rot):
    if letter == "-":
        return " "
    if letter == " ":
        return "-"
    shift = ord('a') if letter.islower() else ord('A')
    return chr((ord(letter) - shift + rot) % 26 + shift)


lines = []
with open("input_4.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match(r"(.*)-([0-9]+)\[(.{5})\]", line)
        if m:
            name = m.group(1)
            room_number = int(m.group(2))
            checksum = m.group(3)
            lines.append((name, room_number, checksum))

sum_room_numbers = 0
for name, room_number, checksum in lines:
    c = Counter(name.replace("-", ""))
    most_common_letters = sorted(c.most_common(), key=lambda x: (-x[1], x[0]))
    most_common_letters = "".join([char[0] for char in most_common_letters[:5]])
    if most_common_letters == checksum:
        sum_room_numbers += room_number
        decrypted_name = "".join([rotate(c, room_number) for c in name])
        if decrypted_name == "northpole object storage":
            print("PART 2")
            print(room_number)

print("PART 1")
print(sum_room_numbers)

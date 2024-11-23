map = []
with open("input_19.txt") as file:
    for line in file:
        line = line[:-1]
        map.append(line)


def valid_move(pos):
    if pos.real < 0 or pos.real >= len(map):
        return False
    if pos.imag < 0 or pos.imag >= len(map[int(pos.real)]):
        return False
    return True

def cell(pos):
    return map[int(pos.real)][int(pos.imag)]

pos = 0 + 0j
direction = 1 + 0j
visited = ""
num_steps = 0

while cell(pos) == " ":
    pos += 1j

while True:
    current_char = cell(pos)
    if current_char.isalnum():
        visited += current_char

    if valid_move(pos + direction) and cell(pos + direction) != " ":
        pos += direction
        num_steps += 1
    else:
        turned = False
        for newDirection in [1, -1, 1j, -1j]:
            if valid_move(pos + newDirection) and cell(pos + newDirection) != " " and newDirection != direction * -1:
                direction = newDirection
                turned = True
                break
        if not turned:
            break

print("PART 1")
print(visited)
print("PART 2")
print(num_steps)

with open("input_1.txt") as file:
    for line in file:
        line = line[:-1]
        instructions = line.split(",")

def walk_instructions(instructions):
    pos = 0 + 0j
    facing = 1 + 0j

    part2_solved = False
    pos_visited = []

    for instruction in instructions:
        instruction = instruction.strip()
        direction, length = instruction[:1], int(instruction[1:])
        if direction == "R":
            facing *= 0 + 1j
        else:
            facing *= 0 - 1j

        for i in range(length):
            pos += facing

            if pos in pos_visited and not part2_solved:
                print("PART 2")
                print(int(abs(pos.real) + abs(pos.imag)))
                part2_solved = True

            pos_visited.append(pos)

    print("PART 1")
    print(int(abs(pos.real) + abs(pos.imag)))

walk_instructions(instructions)

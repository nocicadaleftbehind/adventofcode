instructions = []
with open("input_2.txt") as file:
    for line in file:
        instructions.append(line[:-1])
        

def walk_keypad(instructions, keypad):
    pos = [0,0]
    for y, line in enumerate(keypad):
        for x, char in enumerate(line):
            if char == "5":
                pos = [y,x]
                break
  
    code = ""
    for line in instructions:
        for char in line:
            new_pos = [pos[0], pos[1]]
            if char == "U":
                new_pos[1] -= 1
            if char == "D":
                new_pos[1] += 1
            if char == "L":
                new_pos[0] -= 1
            if char == "R":
                new_pos[0] += 1
            pos_char = keypad[new_pos[1]][new_pos[0]]
            if pos_char != " ":
                pos = [new_pos[0], new_pos[1]]
        pos_char = keypad[pos[1]][pos[0]]
        code += str(pos_char)
    return code

keypad_1 = [
    list("     "),
    list(" 123 "),
    list(" 456 "),
    list(" 789 "),
    list("     ")
]

keypad_2 = [
    list("       "),
    list("   1   "),
    list("  234  "),
    list(" 56789 "),
    list("  ABC  "),
    list("   D   "),
    list("       ")
]

print("PART 1")
print(walk_keypad(instructions, keypad_1))
print("PART 2")
print(walk_keypad(instructions, keypad_2))
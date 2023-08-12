input = open("input_1.txt").read()

def part_1(instructions):
    return instructions.count("(") - instructions.count(")")

def part_2(instructions):
    pos = 0
    for char_pos, char in enumerate(instructions, start=1):
        if char == "(":
            pos += 1
        elif char == ")":
            pos -= 1
        if pos == -1:
            return char_pos

    return None

print("PART 1")
print(part_1("(())"))
print(part_1("()()"))
print(part_1("((("))
print(part_1("(()(()("))
print(part_1("))((((("))
print(part_1("())"))
print(part_1("))("))
print(part_1(")))"))
print(part_1(")())())"))
print(part_1(input))

print("PART 2")
print(part_2(")"))
print(part_2("()())"))
print(part_2(input))
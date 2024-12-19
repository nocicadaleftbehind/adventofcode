instructions = []
with open("input_23.txt") as file:
    for line in file:
        line = line[:-1].split(" ")
        instructions.append((line[0], [line[1], line[2]]))

def get_value(registers, string_value):
    if string_value in registers.keys():
        return registers[string_value]
    return int(string_value)

def exec_instruction(opcode, operands, registers):
    operand1 = operands[0]
    operand2 = get_value(registers, operands[1])
    
    if opcode == "set":
        registers[operand1] = operand2
    elif opcode == "sub":
        registers[operand1] -= operand2
    elif opcode == "mul":
        registers[operand1] *= operand2
    elif opcode == "jnz":
        condition = get_value(registers, operand1)
        if condition != 0:
            registers["ip"] += operand2 - 1

def simulate():
    registers = {"ip": 0, "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
    num_muls = 0
    while True:
        instruction = instructions[registers["ip"]]
        opcode, operands = instruction
        if opcode == "mul":
            num_muls += 1
        exec_instruction(opcode, operands, registers)
        registers["ip"] += 1
        if registers["ip"] < 0 or registers["ip"] >= len(instructions):
            break
    return num_muls

def shortcut():
    h = 0
    for x in range(108100, 125101, 17):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
    return h

print("PART 1")
print(simulate())
print("PART 2")
print(shortcut())

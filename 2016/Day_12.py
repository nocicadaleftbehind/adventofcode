import re

program = []
with open("input_12.txt") as file:
    for line in file:
        line = line[:-1]
        program.append(line)

def execute(line, registers):
    m = re.match("cpy (.+) (.+)", line)
    if m:
        source = m.group(1)
        target = m.group(2)
        return execute_cpy(registers, source, target)
    m = re.match("inc (.+)", line)
    if m:
        target = m.group(1)
        return execute_inc(registers, target)
    m = re.match("dec (.+)", line)
    if m:
        target = m.group(1)
        return execute_dec(registers, target)
    m = re.match("jnz (.+) (.+)", line)
    if m:
        condition = m.group(1)
        target = m.group(2)
        return execute_jnz(registers, condition, target)
    
    print("Invalid operation", line)
    return registers


def execute_cpy(registers, source, target):
    if source.isdigit():
        source = int(source)
    else:
        source = registers[source]
    registers[target] = source
    registers["ip"] += 1
    return registers


def execute_inc(registers, target):
    registers[target] += 1
    registers["ip"] += 1
    return registers


def execute_dec(registers, target):
    registers[target] -= 1
    registers["ip"] += 1
    return registers


def execute_jnz(registers, condition, target):
    if condition.isdigit():
        value = int(condition)
    else:
        value = registers[condition]
    
    if value != 0:
        target = int(target)
        registers["ip"] += target
    else:
        registers["ip"] += 1
    return registers

def execute_program(lines, registers):
    while True:
        instruction = lines[registers["ip"]]
        registers = execute(instruction, registers)
        if 0 < registers["ip"] >= len(lines):
            break
    return registers["a"]

print("PART 1")
registers = {"a": 0, "b": 0, "c": 0, "d": 0, "ip": 0}
print(execute_program(program, registers))

print("PART 2")
registers = {"a": 0, "b": 0, "c": 1, "d": 0, "ip": 0}
print(execute_program(program, registers))

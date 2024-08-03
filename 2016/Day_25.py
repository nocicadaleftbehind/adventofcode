from pprint import pprint

import re

import itertools

program = []

with open("input_25.txt") as file:
    for line in file:
        line = line[:-1]
        program.append(line.split(" "))


def get_value(registers, source):
    if source.startswith("-"):
        source = -int(source[1:])
    elif source.isdigit():
        source = int(source)
    else:
        source = registers[source]
    return source


def execute(program, registers):
    line = program[registers["ip"]]

    opcode = line[0]
    if opcode == "cpy":
        registers = execute_cpy(registers, line[1], line[2])
    elif opcode == "inc":
        registers = execute_inc(registers, line[1])
    elif opcode == "dec":
        registers = execute_dec(registers, line[1])
    elif opcode == "jnz":
        registers = execute_jnz(registers, line[1], line[2])
    elif opcode == "tgl":
        registers = execute_tgl(program, registers, line[1])
    elif opcode == "out":
        registers = execute_out(registers, line[1])
    return registers


def execute_cpy(registers, source, target):
    registers["ip"] += 1
    source = get_value(registers, source)
    if target not in registers.keys():
        return registers
    registers[target] = source
    return registers


def execute_inc(registers, target):
    registers["ip"] += 1
    registers[target] += 1
    return registers


def execute_tgl(program, registers, target):
    registers["ip"] += 1
    value = get_value(registers, target)
    target = value + (registers["ip"] - 1)
    if target < 0 or target >= len(program):
        return registers
    line_to_change = program[target]
    if len(line_to_change) == 2:
        if line_to_change[0] == "inc":
            line_to_change[0] = "dec"
        else:
            line_to_change[0] = "inc"
    else:
        if line_to_change[0] == "jnz":
            line_to_change[0] = "cpy"
        else:
            line_to_change[0] = "jnz"
    program[target] = line_to_change
    return registers


def execute_dec(registers, target):
    registers["ip"] += 1
    registers[target] -= 1
    return registers


def execute_jnz(registers, condition, target):
    value = get_value(registers, condition)
    if value != 0:
        target = get_value(registers, target)
        registers["ip"] += target
    else:
        registers["ip"] += 1
    return registers

def execute_out(registers, target):
    registers["ip"] += 1
    value = get_value(registers, target)
    registers["out"].append(value)
    return registers


def check_if_alternating(s):
    if s.count(0) + s.count(1) != len(s):
        return False
    if s[0] == 1:
        return False
    for a, b in zip(s, s[1:]):
        if a == b:
            return False
    return True

def part_1():
    for i in itertools.count():
        registers = {"a": i, "b": 0, "c": 0, "d": 0, "ip": 0, "out": []}
        while True:
            registers = execute(program, registers)
            if registers["ip"] >= len(program):
                break
            if len(registers["out"]) >= 20:
                if check_if_alternating(registers["out"]):
                    return i
                break

print("PART 1")
print(part_1())
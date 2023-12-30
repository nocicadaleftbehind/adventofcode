import re

instructions = []
with open("input_23.txt") as file:
    for line in file:
        line = line[:-1]
        instructions.append(line)


def execute_instruction(line):
    global a, b, ip
    m = re.match("hlf (.+)", line)
    if m:
        return hlf(m)
    m = re.match("tpl (.+)", line)
    if m:
        return tpl(m)
    m = re.match("inc (.+)", line)
    if m:
        return inc(m)
    m = re.match("jmp (.+)", line)
    if m:
        return jmp(m)
    m = re.match("jie (.+), (.+)", line)
    if m:
        return jie(m)
    m = re.match("jio (.+), (.+)", line)
    if m:
        return jio(m)
    else:
        print("INVALID OPCODE")
        print(line)
        exit(-1)


def hlf(m):
    global a, b, ip
    register_name = m.group(1)
    if register_name == "a":
        a //= 2
    elif register_name == "b":
        b //= 2
    ip += 1


def tpl(m):
    global a, b, ip
    register_name = m.group(1)
    if register_name == "a":
        a *= 3
    elif register_name == "b":
        b *= 3
    ip += 1


def inc(m):
    global a, b, ip
    register_name = m.group(1)
    if register_name == "a":
        a += 1
    elif register_name == "b":
        b += 1
    ip += 1


def jmp(m):
    global a, b, ip
    offset = m.group(1)
    offset = int(offset)
    ip += offset


def jie(m):
    global a, b, ip
    register_name = m.group(1)
    cond = False
    if register_name == "a":
        cond = (a % 2 == 0)
    elif register_name == "b":
        cond = (b % 2 == 0)
    offset = m.group(2)
    offset = int(offset)
    if cond:
        ip += offset
    else:
        ip += 1


def jio(m):
    global a, b, ip
    register_name = m.group(1)
    cond = False
    if register_name == "a":
        cond = (a == 1)
    elif register_name == "b":
        cond = (b == 1)
    offset = m.group(2)
    offset = int(offset)
    if cond:
        ip += offset
    else:
        ip += 1

a = 1
b = 0
ip = 0
while True:
    if ip < 0 or ip >= len(instructions):
        print(a, b)
        break
    current_instruction = instructions[ip]
    execute_instruction(current_instruction)

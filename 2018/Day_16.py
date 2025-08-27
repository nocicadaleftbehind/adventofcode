import re
from collections import defaultdict

test_cases = []
with open("input_16.txt") as file:
    lines = file.readlines()
    input_data = []
    operation = []
    output_data = []
    
    end_of_block = 0
    for i, line in enumerate(lines):
        if i % 4 == 0:
            if not line.startswith("Before:"):
                end_of_block = i
                break
            m = re.match(r"Before: \[(\d+), (\d+), (\d+), (\d+)\]", line)
            input_data = list(map(int, [m.group(1), m.group(2), m.group(3), m.group(4)]))
        if i % 4 == 1:
            operation = list(map(int, line.split(" ")))
        if i % 4 == 2:
            m = re.match(r"After:  \[(\d+), (\d+), (\d+), (\d+)\]", line)
            output_data = list(map(int, [m.group(1), m.group(2), m.group(3), m.group(4)]))
        if i % 4 == 3:
            test_cases.append((input_data, operation, output_data))
    
    program = []
    for line in lines[end_of_block + 2:]:
        program.append([int(c) for c in line.split(" ")])

def apply_op(parameters, rin, fun):
    rout = [*rin]
    rout[parameters[3]] = fun( (parameters[1], parameters[2]) )
    return rout

def addr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + rin[p[1]])

def addi(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + p[1])

def mulr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * rin[p[1]])

def muli(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * p[1])

def banr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] & rin[p[1]])
    
def bani(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] & p[1])

def borr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] | rin[p[1]])

def bori(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] | p[1])

def setr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]])

def seti(parameters, rin):
    return apply_op(parameters, rin, lambda p: p[0])

def gtir(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if p[0] > rin[p[1]] else 0)

def gtri(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] > p[1] else 0)

def gtrr(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] > rin[p[1]] else 0)
    
def eqir(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if p[0] == rin[p[1]] else 0)

def eqri(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] == p[1] else 0)

def eqrr(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] == rin[p[1]] else 0)


passing_testcases = defaultdict(set)
ambiguous_testcases = 0
for in_data, opcode, out_data in test_cases:
    test_pass = 0
    for ops in [eqri, bani, seti, bori, eqir, banr, borr, muli, setr, addr, eqrr, addi, gtir, gtrr, gtri, mulr]:
        if ops(opcode, in_data) == out_data:
            test_pass += 1
            passing_testcases[opcode[0]].add(ops)
    if test_pass >= 3:
        ambiguous_testcases += 1
print("PART 1")
print(ambiguous_testcases)

operations_by_number = {}
while len(operations_by_number.keys()) < 16:
    unambiguous = {k:v for k, v in passing_testcases.items() if len(passing_testcases[k]) == 1}
    for opcode, ops in unambiguous.items():
        op = ops.pop()
        operations_by_number[opcode] = op
        del passing_testcases[opcode]
        for k in passing_testcases.keys():
            if op in passing_testcases[k]:
                passing_testcases[k].remove(op)

registers = [0, 0, 0, 0]
for line in program:
    opcode = line[0]
    ops = operations_by_number[opcode]
    registers = ops(line, registers)
print("PART 2")
print(registers[0])

program = []
with open("input_19.txt") as file:
    for line in file:
        program.append([line.split(" ")[0]] + [int(c) for c in line.split(" ")[1:]])

def apply_op(parameters, rin, fun):
    rin[parameters[2]] = fun((parameters[0], parameters[1]))
    return rin

def addr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + rin[p[1]])


def addi(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + p[1])


def mulr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * rin[p[1]])


def muli(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * p[1])


def setr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]])


def seti(parameters, rin):
    return apply_op(parameters, rin, lambda p: p[0])


def gtrr(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] > rin[p[1]] else 0)


def eqrr(parameters, rin):
    return apply_op(parameters, rin, lambda p: 1 if rin[p[0]] == rin[p[1]] else 0)

operations = {
    "addi": addi,
    "addr": addr,
    "eqrr": eqrr,
    "gtrr": gtrr,
    "muli": muli,
    "mulr": mulr,
    "seti": seti,
    "setr": setr
}

operation = program.pop(0)
opcode, ip = operation
if opcode == "#ip":
    ip = operation[1]

def run_program(a_init, quick_exit=False):
    registers = [a_init, 0, 0, 0, 0, 0]

    while True:
        operation = program[registers[ip]]
        opcode, *parameters = operation
        function = operations[opcode]
        registers = function(parameters, registers)
        if registers[ip] == 2 and quick_exit:
            break
        registers[ip] += 1
        if registers[ip] < 0 or registers[ip] >= len(program):
            break
    
    if quick_exit:
        return sum([x for x in range(1, registers[2] + 1) if registers[2] % x == 0])
    return registers[0]

print("PART 1")
print(run_program(0, True))

print("PART 2")
print(run_program(1, True))

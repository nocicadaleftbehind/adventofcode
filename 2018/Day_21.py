with open("input_21.txt") as file:
    program = []
    for line in file:
        program.append([line.split(" ")[0]] + [int(c) for c in line.split(" ")[1:]])


def apply_op(parameters, rin, fun):
    rin[parameters[2]] = fun((parameters[0], parameters[1]))
    return rin


def addi(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + p[1])


def addr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] + rin[p[1]])


def bani(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] & p[1])


def banr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] & rin[p[1]])


def bori(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] | p[1])


def borr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] | rin[p[1]])


def mulr(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * rin[p[1]])


def muli(parameters, rin):
    return apply_op(parameters, rin, lambda p: rin[p[0]] * p[1])


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


operations = {
    "addi": addi,
    "addr": addr,
    "bani": bani,
    "banr": banr,
    "bori": bori,
    "borr": borr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
    "gtir": gtir,
    "gtri": gtri,
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
    
def simulate_program(a_init):
    registers = [a_init, 0, 0, 0, 0, 0]
    num_operations = 0

    while True:
        operation = program[registers[ip]]
        opcode, *parameters = operation
        function = operations[opcode]
        registers = function(parameters, registers)
        registers[ip] += 1
        num_operations += 1
        if registers[ip] < 0 or registers[ip] >= len(program):
            break

    return registers[0]

def decompiled_program():
    r3 = 0
    r3_values = []
    while True:
        r2 = r3 | 65536
        r3 = 1099159

        while True:
            r1 = r2 & 255
            r3 = r3 + r1
            r3 = r3 & 16777215
            r3 = r3 * 65899
            r3 = r3 & 16777215

            if 256 > r2:
                break
            if r2 % 256 == 0:
                r2 = (r2 - 1) // 256 + 1
            else:
                r2 = (r2 - 1) // 256

        if r3 in r3_values:
            return r3_values
        r3_values.append(r3)

compared_values = decompiled_program()

print("PART 1")
print(compared_values[0])
print("PART 2")
print(compared_values[-1])

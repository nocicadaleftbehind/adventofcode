import string

instructions = []
with open("input_18.txt") as file:
    for line in file:
        line = line[:-1]
        operation = line.split(" ")[0]
        values = line.split(" ")[1:]
        instructions.append((operation, values))


def get_value(registers, value):
    if value in registers.keys():
        value = registers[value]
    else:
        value = int(value)
    return value


def exec_instruction(instruction, register, sound_queue):
    opcode, values = instruction
    first_reg = values[0]
    first_value = get_value(register, values[0])
    if len(values) > 1:
        second_value = get_value(register, values[1])

    if opcode == "snd":
        register["times_send"] += 1
        sound_queue.append(first_value)
    if opcode == "set":
        register[first_reg] = second_value
    if opcode == "add":
        register[first_reg] += second_value
    if opcode == "mul":
        register[first_reg] *= second_value
    if opcode == "mod":
        register[first_reg] = first_value % second_value
    if opcode == "rcv":
        if len(register["sound"]) > 0:
            sound_value = register["sound"].pop(0)
            register[first_reg] = sound_value
            register["wait"] = False
        else:
            register["wait"] = True
            register["ip"] -= 1
        
    if opcode == "jgz":
        if first_value > 0:
            register["ip"] += second_value - 1

    register["ip"] += 1
    return register


def part_1():
    register = {"ip": 0, "sound": [], "wait": False, "times_send": 0}
    for char in string.ascii_lowercase:
        register[char] = 0
    while True:
        instruction = instructions[register["ip"]]
        if instruction[0] == "rcv":
            return register["sound"][-1]
  
        if register["ip"] < 0 or register["ip"] >= len(instructions):
            break
        register = exec_instruction(instruction, register, register["sound"])

def part_2():
    register = [{"ip": 0, "sound": [], "wait": False, "times_send": 0},
                {"ip": 0, "sound": [], "wait": False, "times_send": 0}]
    for i in [0, 1]:
        for char in string.ascii_lowercase:
            register[i][char] = 0
        register[i]["p"] = i
    
    while True:
        for i in [0, 1]:
            instruction = instructions[register[i]["ip"]]
            register[i] = exec_instruction(instruction, register[i], register[1 - i]["sound"])
            if register[i]["ip"] < 0 or register[i]["ip"] >= len(instructions):
                break
        if register[0]["wait"] and register[1]["wait"]:
            return register[1]["times_send"]

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

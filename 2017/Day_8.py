import re
from collections import defaultdict

program = []
with open("input_8.txt") as file:
    for line in file:
        line = line[:-1]
        program.append(line)

def comparison(op, v1, v2):
    if op == "==":
        return v1 == v2
    if op == "!=":
        return v1 != v2
    if op == "<":
        return v1 < v2
    if op == "<=":
        return v1 <= v2
    if op == ">":
        return v1 > v2
    if op == ">=":
        return v1 >= v2

registers = defaultdict(int)
highest_value = 0
for line in program:
    m = re.match("(.+) (.+) (.+) if (.+) (.+) (.+)", line)
    if not m:
        continue
    register_name = m.group(1)
    direction = m.group(2)
    amount = int(m.group(3))
    comp_register = m.group(4)
    operator = m.group(5)
    value2 = int(m.group(6))
    if direction == "dec":
        amount *= -1
    value1 = registers[comp_register]
    if comparison(operator, value1, value2):
        registers[register_name] += amount

    highest_value = max(highest_value, max(registers.values()))

print("PART 1")
print(max(registers.values()))
print("PART 2")
print(highest_value)

import pprint
import re

from collections import defaultdict


def parse_formula(string):
    if string in wire_values:
        return wire_values[string]
    m = re.match("(-?[0-9]+)$", string)
    if m:
        return int(m.group(1))
    m = re.match("^([a-z]+)$", string)
    if m:
        var_name = m.group(1)
        if var_name in wire_values:
            return wire_values[var_name]
        else:
            value = parse_formula(wire_formulas[var_name])
            wire_values[var_name] = value
            return value
    m = re.match("NOT (.*)$", string)
    if m:
        operand = parse_formula(m.group(1))
        return 2**16 - 1 - operand
    m = re.match("(.*) OR (.*)$", string)
    if m:
        operand1 = parse_formula(m.group(1))
        operand2 = parse_formula(m.group(2))
        return operand1 | operand2
    m = re.match("(.*) AND (.*)$", string)
    if m:
        operand1 = parse_formula(m.group(1))
        operand2 = parse_formula(m.group(2))
        return operand1 & operand2
    m = re.match("(.*) RSHIFT (.*)$", string)
    if m:
        operand1 = parse_formula(m.group(1))
        operand2 = parse_formula(m.group(2))
        return operand1 >> operand2
    m = re.match("(.*) LSHIFT (.*)$", string)
    if m:
        operand1 = parse_formula(m.group(1))
        operand2 = parse_formula(m.group(2))
        return operand1 << operand2
    return 0


wire_formulas = defaultdict(int)
wire_values = {}
with open("input_7.txt") as file:
    for line in file:
        formula, output = line.split(" -> ")
        output = output[:-1]
        wire_formulas[output] = formula

print(parse_formula('a'))
wire_values = {"b": parse_formula('a')}
print(parse_formula('a'))

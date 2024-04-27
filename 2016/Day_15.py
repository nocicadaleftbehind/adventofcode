import re
from functools import reduce

discs = []

with open("input_15.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).", line)
        if m:
            num_positions = int(m.group(1))
            current_position = int(m.group(2))
            discs.append((num_positions, current_position))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_start_time(discs):
    divisors = [t[0] for t in discs]
    remainders = [t[0] - (t[1] + i + 1) % t[0] for i, t in enumerate(discs)]
    return chinese_remainder(divisors, remainders)


print("PART 1")
print(find_start_time(discs))

print("PART 2")
discs.append((11, 0))
print(find_start_time(discs))

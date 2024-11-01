with open("input_15.txt") as f:
    lines = f.readlines()
    start_a = int(lines[0].split(" ")[-1])
    start_b = int(lines[1].split(" ")[-1])

a_factor = 16807
b_factor = 48271
mod = 2147483647

def count_matches(a, b, limit, use_mod):
    matches = 0
    for i in range(limit + 1):
        a = (a * a_factor) % mod
        if use_mod:
            while (a % 4) != 0:
                a = (a * a_factor) % mod
        b = (b * b_factor) % mod
        if use_mod:
            while (b % 8) != 0:
                b = (b * b_factor) % mod
        
        lower_a = a & (2 ** 16 - 1)
        lower_b = b & (2 ** 16 - 1)
        if lower_a == lower_b:
            matches += 1
    return matches

print("PART 1")
print(count_matches(start_a, start_b, 40 * 10 ** 6, False))
print("PART 2")
print(count_matches(start_a, start_b, 5 * 10 ** 6, True))


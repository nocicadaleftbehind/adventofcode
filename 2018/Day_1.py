import itertools

frequencies = []
with open("input_1.txt") as file:
    for line in file:
        line = line[:-1]
        line = int(line.replace("+", ""))
        frequencies.append(line)

def part_1():
    return sum(frequencies)

def part_2():    
    freqs = set()
    freq = 0
    for l in itertools.cycle(frequencies):
        freq += l
        if freq in freqs:
            return freq
        freqs.add(freq)

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

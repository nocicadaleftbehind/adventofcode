import itertools

container_sizes = []
with open("input_17.txt") as file:
    for line in file:
        value = int(line[:-1])
        container_sizes.append(value)

def part_1(container_sizes):
    total = 0
    for size in range(len(container_sizes)):
        for subset in itertools.combinations(container_sizes, size):
            if sum(subset) == 150:
                total += 1
    return total


def part_2(container_sizes):
    for size in range(len(container_sizes)):
        num_correct_sizes = 0
        for subset in itertools.combinations(container_sizes, size):
            if sum(subset) == 150:
                num_correct_sizes += 1

        if num_correct_sizes > 0:
            return num_correct_sizes

print("PART 1")
print(part_1(container_sizes))
print("PART 2")
print(part_2(container_sizes))



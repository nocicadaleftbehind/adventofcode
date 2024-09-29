from functools import reduce

LIST_SIZE = 256

with open("input_10.txt") as file:
    for line in file:
        input_line = line[:-1]


def hash_string(array, lengths, num_rounds):
    current_position = 0
    skip_size = 0
    for round in range(num_rounds):
        for length in lengths:
            sublist = (array + array)[current_position: current_position + length]
            for pos, value in enumerate(reversed(sublist)):
                pos = (current_position + pos) % LIST_SIZE
                array[pos] = value
            current_position = (current_position + length + skip_size) % LIST_SIZE
            skip_size += 1
    return array

def sparse_to_dense(sparse):
    hex_string = []
    for x in range(16):
        subslice = sparse[16 * x:16 * (x + 1)]
        hex_string.append('%02x' % reduce((lambda x, y: x ^ y), subslice))
    return "".join(hex_string)


def part_1():
    lengths = [int(c) for c in input_line.split(",")]
    array = list(range(LIST_SIZE))
    a = hash_string(array, lengths, 1)
    return a[0] * a[1]


def part_2():
    lengths = [ord(c) for c in input_line]
    lengths += [17, 31, 73, 47, 23]
    array = list(range(LIST_SIZE))

    s = hash_string(array, lengths, 64)
    return sparse_to_dense(s)

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

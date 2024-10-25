from functools import reduce


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


def knot_hash(input_line):
    lengths = [ord(c) for c in input_line]
    lengths += [17, 31, 73, 47, 23]
    array = list(range(LIST_SIZE))

    s = hash_string(array, lengths, 64)
    return sparse_to_dense(s)


def hash_to_binary(hash):
    bin_string = bin(int(hash, 16))
    return list(bin_string)[2:]


def count_bits(grid):
    total = 0
    for l in grid:
        total += l.count("1")
    return total


def fill(grid, i, j):
    grid[i][j] = "0"
    neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for x, y in neighbours:
        if 0 <= x < 128 and 0 <= y < 128:
            if grid[x][y] == "1":
                fill(grid, x, y)


def count_regions(grid):
    num_regions = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                num_regions += 1
                fill(grid, i, j)
    return num_regions


def create_grid(salt):
    grid = []
    for i in range(128):
        string = salt + "-" + str(i)
        hash = knot_hash(string)
        binary_string = hash_to_binary(hash)
        binary_string = ["0"] * (128 - len(binary_string)) + binary_string
        grid.append(binary_string)
    return grid


input_salt = open("input_14.txt").read().strip()
LIST_SIZE = 256

grid = create_grid(input_salt)
print("PART 1")
print(count_bits(grid))
print("PART 2")
print(count_regions(grid))

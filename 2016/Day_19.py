num_elves = int(open("input_19.txt").read())


def solve_part_one(num_elves):
    elves = list(range(1, num_elves + 1))
    while len(elves) > 1:
        offset = len(elves) % 2
        elves = elves[::2]
        if offset:
            elves = elves[1:]
    return elves[0]


def solve_part_two(num_elves):
    i = 1
    while i * 3 < num_elves:
        i *= 3
    if num_elves > 2 * i:
        return 2 * num_elves - 3 * i
    return num_elves - i


print("PART 1")
print(solve_part_one(num_elves))
print("PART 2")
print(solve_part_two(num_elves))

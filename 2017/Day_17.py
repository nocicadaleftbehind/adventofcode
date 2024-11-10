num_steps = int(open("input_17.txt").read())


def part_1():
    ringbuffer = [0]
    current_pos = 0
    for i in range(1, 2017 + 1):
        current_pos = (current_pos + num_steps) % i
        ringbuffer.insert(current_pos + 1, i)
        current_pos += 1
    return ringbuffer[(current_pos + 1) % i]

def part_2():
    current_pos = 0
    value_after_0 = 0
    for i in range(1, 50000000 + 1):
        current_pos = (current_pos + num_steps) % i
        if current_pos == 0:
            value_after_0 = i
        current_pos += 1
    return value_after_0

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

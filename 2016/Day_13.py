import heapq

INPUT = int(open("input_13.txt").read())

GOAL_X = 31
GOAL_Y = 39


def valid_move(x, y):
    number = x * x + 3 * x + 2 * x * y + y + y * y + INPUT
    bit_string = bin(number)
    number_ones = bit_string.count("1")
    if number_ones % 2 == 0:
        return True
    else:
        return False


def end_state(x, y):
    if x == GOAL_X and y == GOAL_Y:
        return True
    return False


def generate_states(x, y):
    new_states = []
    for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if x < 0 or y < 0:
            continue
        if valid_move(x, y):
            yield x, y
    return new_states


def state_heuristic(x, y):
    return abs(GOAL_X - x) + abs(GOAL_Y - y)


def part_1():
    visited = set()
    queue = []
    heapq.heappush(queue, (0, 0, 1, 1))
    while len(queue) > 0:
        heuristic, length, x, y = heapq.heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if end_state(x, y):
            return length

        new_state_list = generate_states(x, y)
        for nx, ny in new_state_list:
            heuristic = state_heuristic(nx, ny)
            heapq.heappush(queue, (length + heuristic, length + 1, nx, ny))
            
def part_2():
    visited = set()
    queue = []
    heapq.heappush(queue, (0, 0, 1, 1))
    while len(queue) > 0:
        heuristic, length, x, y = heapq.heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if length > 49:
            continue

        new_state_list = generate_states(x, y)
        for nx, ny in new_state_list:
            heuristic = state_heuristic(nx, ny)
            heapq.heappush(queue, (length + heuristic, length + 1, nx, ny))
    return len(visited)

print("PART 1")
print(part_1())

print("PART 2")
print(part_2())

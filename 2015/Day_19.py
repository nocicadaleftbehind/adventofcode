import heapq
import re

starting_string = ""
rules_forward = []
rules_backward = []
with open("input_19.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("(.+) => (.+)", line)
        if m:
            start = m.group(1)
            end = m.group(2)
            rules_forward.append((start, end))
            rules_backward.append((end, start))
        else:
            starting_string = line


def replace_n(string, pattern, replacement, n):
    pattern_len = len(pattern)
    current_pattern = 0
    current_start = 0
    while current_pattern <= n:
        index = string.find(pattern, current_start)
        if current_pattern == n:
            return string[:index] + replacement + string[index + pattern_len:]
        else:
            current_start = index + 1
            current_pattern += 1
    return string


def find_all_replacements(string, rules):
    results = set()
    for pattern, replacement in rules:
        num_patterns = string.count(pattern)
        for i in range(num_patterns):
            replaced = replace_n(string, pattern, replacement, i)
            results.add(replaced)
    return results


print("PART 1")
print(len(find_all_replacements(starting_string, rules_forward)))

print("PART 2")
queue = [(0, 0, starting_string)]
visited = set()
while len(queue) > 0:
    _, current_length, current_string = heapq.heappop(queue)
    if current_string == "e":
        print(current_length)
        break
    if current_string in visited:
        continue
    visited.add(current_string)
    for replaced in find_all_replacements(current_string, rules_backward):
        if replaced in visited:
            continue
        heapq.heappush(queue, (len(replaced) + current_length, current_length + 1, replaced))

print("HEURISTIC")
num_symbols = sum([1 for c in starting_string if c.isupper()])
num_rn = starting_string.count("Rn")
num_ar = starting_string.count("Ar")
num_y = starting_string.count("Y")
print(num_symbols - num_ar - num_rn - 2 * num_y - 1)

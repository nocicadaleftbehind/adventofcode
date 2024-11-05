import re

instructions = []
with open("input_16.txt") as file:
    for line in file:
        line = line[:-1]
        line = line.split(",")
        instructions += line

def dance(programs):
    for instruction in instructions:
        m = re.match("s(\d+)", instruction)
        if m:
            size = int(m.group(1))
            programs = programs[-size:] + programs[:-size]
            continue
        m = re.match("x(.+)/(.+)", instruction)
        if m:
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
            continue
        m = re.match("p(.+)/(.+)", instruction)
        if m:
            pos1 = programs.index(m.group(1))
            pos2 = programs.index(m.group(2))
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
            continue
    return programs

def hash_programs(programs):
    return "".join(programs)

def run_many_rounds():
    programs = list("abcdefghijklmnop")
    seen = [hash_programs(programs)]
    loop_size = 0
    for i in range(10**9):
        programs = dance(programs)
        h = hash_programs(programs)
        if h in seen:
            loop_size = len(seen) - seen.index(h)
            break
        seen.append(h)
    return seen[10 ** 9 % loop_size] 

print("PART 1")
print(hash_programs(dance(list("abcdefghijklmnop"))))
print("PART 2")
print(run_many_rounds())
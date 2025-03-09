import copy
import itertools
from collections import defaultdict
import re

requirements = defaultdict(set)
tasks = set()
with open("input_7.txt") as file:
    for line in file:
        m = re.search("Step (.) must be finished before step (.) can begin.", line)
        if m:
            source = m.group(1)
            target = m.group(2)
            requirements[target].add(source)
            tasks = tasks.union([source, target])

def part_1(requirements, tasks):
    open_tasks = list(sorted(copy.copy(tasks)))
    solved_tasks = set()
    order = ""
    while len(open_tasks) > 0:
        for task in open_tasks:
            if requirements[task] <= solved_tasks:
                solved_tasks.add(task)
                order += task
                open_tasks.remove(task)
                break
    return order

def part_2(requirements, tasks):
    tasks = sorted(tasks)
    requirements = copy.deepcopy(requirements)
    
    done = set()
    working = []
    num_free_workers = 5
    for time_step in itertools.count():
        if len(working) == 0 and len(tasks) == 0:
            break
        for task in tasks:
            if task in done:
                continue
            can_start = num_free_workers > 0
            for req in requirements[task]:
                if req not in done:
                    can_start = False
                    break
            if can_start:
                working.append((61 + ord(task) - ord('A'), task))
                num_free_workers -= 1
                del requirements[task]
    
        working = [(w[0]-1, w[1]) for w in working]
        for w in working:
            if w[1] in tasks:
                tasks.remove(w[1])
            if w[0] == 0:
                done.add(w[1])
                num_free_workers += 1
        working = [w for w in working if w[0] > 0]
    return time_step

print("PART 1")
print(part_1(requirements, tasks))
print("PART 2")
print(part_2(requirements, tasks))

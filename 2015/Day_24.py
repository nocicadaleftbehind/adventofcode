import itertools
import math
import functools

weights = []
with open("input_24.txt") as file:
    for line in file:
        line = line[:-1]
        weights.append(int(line))

def minimize_subsets(goal):
    accepted_subsets = []
    for i in range(len(weights)):
        for subset in itertools.combinations(weights, i):
            if sum(subset) == goal:
                accepted_subsets.append(subset)
        if len(accepted_subsets) > 0:
            break
    
    min_qe = math.inf
    for subset in accepted_subsets:
        qe = functools.reduce(lambda x, y: x * y, subset, 1)
        min_qe = min(min_qe, qe)
    return min_qe

print("PART 1")
print(minimize_subsets(sum(weights) / 3))
print("PART 2")
print(minimize_subsets(sum(weights) / 4))

import itertools
import numpy

banks = []
with open("input_6.txt") as file:
    for line in file:
        line = line[:-1]
        banks = [int(b) for b in line.split("\t")]

def run_redistribution(start_state):
    state = start_state
    seen_configs = [str(state)]
    for i in itertools.count(1):
        index = numpy.argmax(state)
        value = state[index]
        state[index] = 0
        while value > 0:
            index = (index + 1) % len(state)
            state[index] += 1
            value -= 1
            
        bank_hash = str(state)
        if bank_hash in seen_configs:
            return state, i
        seen_configs.append(bank_hash)

print("PART 1")
state, answer1 = run_redistribution(banks)
print(answer1)
print("PART 2")
_, answer2 = run_redistribution(state)
print(answer2)

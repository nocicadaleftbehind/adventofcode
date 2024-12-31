import re
from collections import defaultdict

RIGHT = 1
LEFT = -1

state = None
num_steps = 0
config = {}
with open("input_25.txt") as f:
    current_state = None
    current_value = None
    next_value = None
    next_direction = None
    next_state = None
    for line in f:
        m = re.match("Begin in state (.*)\.", line)
        if m:
            state = m.group(1)
        
        m = re.match("Perform a diagnostic checksum after (.*) steps.", line)
        if m:
            num_steps = int(m.group(1))
        
        m = re.match("In state (.*):", line)
        if m:
            current_state = m.group(1)
        
        m = re.match(" +If the current value is (.*):", line)
        if m:
            current_value = int(m.group(1))
        
        m = re.match(" +- Write the value (.*).", line)
        if m:
            next_value = int(m.group(1))

        m = re.match(" +- Move one slot to the (.*).", line)
        if m:
            if m.group(1) == "right":
                next_direction = RIGHT
            else:
                next_direction = LEFT

        m = re.match(" +- Continue with state (.*).", line)
        if m:
            next_state = m.group(1)
            config[(current_state, current_value)] = (next_value, next_direction, next_state)

tape = defaultdict(int)
current_location = 0
for i in range(num_steps):
    tape_value = tape[current_location]
    next_value, direction, next_state = config[(state, tape_value)]
    state = next_state
    tape[current_location] = next_value
    current_location += direction
checksum = sum((v for v in tape.values() if v == 1))
print("PART 1")
print(checksum)

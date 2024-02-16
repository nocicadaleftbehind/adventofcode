import re
from collections import defaultdict


bots = {}
inputs = defaultdict(list)
with open("input_10.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("value (\d+) goes to (bot \d+)", line)
        if m:
            value = int(m.group(1))
            bot_number = m.group(2)
            inputs[bot_number].append(value)
        m = re.match("((bot|output) \d+) gives low to ((bot|output) \d+) and high to ((bot|output) \d+)", line)
        if m:
            bot_number = m.group(1)
            output_low = m.group(3)
            output_high = m.group(5)
            bots[bot_number] = (output_low, output_high)

result_1 = None
bot_ids = list(bots.keys())
while True:
    change = False
    for bot_number in bot_ids:
        values = inputs[bot_number]
        if len(values) == 2:
            low = min(values)
            high = max(values)
            
            if low == 17 and high == 61:
                result_1 = bot_number.split(" ")[1]
                
            low_output, high_output = bots[bot_number]
            
            inputs[low_output].append(low)
            inputs[high_output].append(high)
            inputs[bot_number] = []
            
            change = True
    if not change:
        break

print("PART 1")
print(result_1)
print("PART 2")
print(int(inputs["output 2"][0]) * int(inputs["output 1"][0]) * int(inputs["output 0"][0]))

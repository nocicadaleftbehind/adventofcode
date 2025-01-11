import datetime
from collections import defaultdict
import re

lines = []
with open("input_4.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        lines.append(line)

lines = sorted(lines)
current_guard = 0
start = None
intervals = defaultdict(list)
for line in lines:
    m = re.match("\[(.+)\] (.*)", line)
    if m:
        time_stamp = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M")
        text = m.group(2)
        if text == "falls asleep":
            start = time_stamp
        elif text == "wakes up":
            end = time_stamp
            intervals[current_guard].append((start, end))
        else:
            current_guard = int(text.split("#")[1].split(" ")[0])

sleep_schedule = {}
for guard, intervall_list in intervals.items():
    sleeping_minutes = [0] * 60
    for s, e in intervall_list:
        for i in range(s.minute, e.minute):
            sleeping_minutes[i] += 1
    sleep_schedule[guard] = sleeping_minutes

print("PART 1")
most_asleep_guard = max([(sum(s), i) for i, s in sleep_schedule.items()])[1]
guard_schedule = sleep_schedule[most_asleep_guard]
print(most_asleep_guard * guard_schedule.index(max(guard_schedule)))

print("PART 2")
most_asleep_guard = max([(max(s), i) for i, s in sleep_schedule.items()])[1]
guard_schedule = sleep_schedule[most_asleep_guard]
print(most_asleep_guard * guard_schedule.index(max(guard_schedule)))

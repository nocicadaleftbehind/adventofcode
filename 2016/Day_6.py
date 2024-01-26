from collections import Counter

NUM_COLUMNS = 8
columns = ["" for i in range(NUM_COLUMNS)]

lines = []
with open("input_6.txt") as file:
    for line in file:
        lines.append(line.strip())

columns = []
for i in range(len(lines[0])):
    columns.append([line[i] for line in lines])

def most_common(columns, position):
    solution = ""
    for column in columns:
        c = Counter(column)
        char = c.most_common()[position][0]
        solution += char
    return solution

print("PART 1")
print(most_common(columns, 0))
print("PART 2")
print(most_common(columns, -1))

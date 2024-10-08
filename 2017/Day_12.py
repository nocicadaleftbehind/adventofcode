groups = []
with open("input_12.txt") as file:
    for line in file:
        line = line.replace("<->", ",")
        member = set([int(i) for i in line.split(",")])
        groups.append(member)

while True:
    no_change = True
    for i in range(len(groups)):
        if len(groups[i]) == 0:
            continue
        for j in range(i + 1, len(groups)):
            if groups[i] & groups[j] != set():
                groups[i] = groups[i] | groups[j]
                groups[j] = set()
                no_change = False
    if no_change:
        break
    groups = [g for g in groups if len(g) > 0]

for g in groups:
    if 0 in g:
        print("PART 1")
        print(len(g))
        break
print("PART 2")
print(len(groups))

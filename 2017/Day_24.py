parts = []
with open("input_24.txt") as file:
    for line in file:
        line = line[:-1]
        left, right = line.split("/")
        parts.append((int(left), int(right)))

def generate_bridges(bridge_head, last_connection, available_parts):
    for i, part in enumerate(available_parts):
        if part[0] == last_connection:
            next_connection = part[1]
        elif part[1] == last_connection:
            next_connection = part[0]
        else:
            continue
        yield bridge_head + [part]
        
        yield from generate_bridges(bridge_head + [part], next_connection, available_parts[:i] + available_parts[i + 1:])


max_length_strength = 0
max_strength = 0
max_length = 0
for bridge in generate_bridges([], 0, parts):
    strength = sum([sum(part) for part in bridge])
    max_strength = max(max_strength, strength)
    
    if len(bridge) >= max_length:
        max_length_strength = max(max_length_strength, strength)
        max_length = len(bridge)

print("PART 1")
print(max_strength)
print("PART 2")
print(max_length_strength)


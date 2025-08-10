import copy
import itertools

original_grid = []
with open("input_15.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        original_grid.append(list(line))

units = []
for y, line in enumerate(original_grid):
    for x, cell in enumerate(line):
        if cell in "EG":
            units.append({"pos": x + y * 1j, "hp": 200, "attack": 3, "type": cell, "active": False})


def neighbors(pos, cell_types, grid):
    cells = [pos + delta for delta in [-1j, -1, 1, 1j] if
             grid[int((pos + delta).imag)][int((pos + delta).real)] in cell_types]
    return cells

def flatten(xss):
    return [x for xs in xss for x in xs]

def find_path(start, target_cells, grid):
    queue = [[start]]
    visited = set()
    candidates = []
    
    while len(queue) > 0:
        path = queue.pop(0)
        end_cell = path[-1]
        
        if len(candidates) > 0 and len(path) > len(candidates[0]):
            break

        if end_cell in visited:
            continue
        visited.add(end_cell)
        if end_cell in target_cells:
            candidates.append(path)
            continue

        for next_cell in neighbors(end_cell, ".", grid):
            if next_cell in path:
                continue
            queue.append(path + [next_cell])

    if len(candidates) == 0:
        return [start, start]
    
    candidates = list(sorted(candidates, key=lambda p: (p[-1].imag, p[-1].real)))
    return candidates[0]


def simulate_combat(original_units):
    grid = copy.deepcopy(original_grid)
    units = copy.deepcopy(original_units)

    for round in itertools.count(1):
        for unit in units:
            if len(set([u["type"] for u in units])) == 1:
                break
            
            unit["active"] = True
            if unit["hp"] <= 0:
                continue
            
            other_type = "E" if unit["type"] == "G" else "G"
            enemy_cell = neighbors(unit["pos"], other_type, grid)
    
            if len(enemy_cell) == 0:
                enemy_pos = flatten([neighbors(e["pos"], "." + other_type, grid) for e in units if (e["type"] == other_type and e["hp"] > 0)])
                path_to_enemy = find_path(unit["pos"], enemy_pos, grid)
                next_cell = path_to_enemy[1]
                grid[int(unit["pos"].imag)][int(unit["pos"].real)] = "."
                grid[int(next_cell.imag)][int(next_cell.real)] = unit["type"]
                unit["pos"] = next_cell
            
            enemy_cells = neighbors(unit["pos"], other_type, grid)
            if len(enemy_cells) > 0:
                target_units = [u for u in units if u["pos"] in enemy_cells]
                target_units = list(sorted(target_units, key=lambda u: (u["hp"], u["pos"].imag, u["pos"].real)))
                target_unit = target_units[0]
                
                target_unit["hp"] -= unit["attack"]
                if target_unit["hp"] <= 0:
                    grid[int(target_unit["pos"].imag)][int(target_unit["pos"].real)] = "."
    
            if len(set([u["type"] for u in units if u["hp"] > 0])) == 1:
                break
    
        units = sorted([u for u in units if u["hp"] > 0], key=lambda u: (u["pos"].imag, u["pos"].real))
    
        if len(set([u["type"] for u in units])) == 1:
            full_rounds = round
            if len([u for u in units if u["active"] == False]) > 0:
                full_rounds -= 1
            return units[0]["type"], full_rounds * sum([u["hp"] for u in units]), len([u for u in units if u["type"] == "E"])
            
        for unit in units:
            unit["active"] = False

winner, points, _ = simulate_combat(units)
print("PART 1")
print(points)

print("PART 2")
num_elves = len([u for u in units if u["type"] == "E"])
for attack in itertools.count(3):
    for unit in units:
        if unit["type"] == "E":
            unit["attack"] = attack
    winner, points, elves_remaining = simulate_combat(units)
    if winner == "E" and elves_remaining == num_elves:
        print(points)
        break

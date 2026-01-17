import copy
import itertools

OPEN = "."
TREE = "|"
LUMBERYARD = "#"

initial_grid = []
with open("input_18.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        initial_grid.append(list(line))


def get_surroundings(grid, x, y):
    l = []
    for ny, nx in [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                   (y, x - 1), (y, x + 1),
                   (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            l.append(grid[ny][nx])
    return l


def run_iteration(grid):
    new_grid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            surroundings = get_surroundings(grid, x, y)
            if grid[y][x] == OPEN and surroundings.count(TREE) >= 3:
                new_grid[y][x] = TREE
            elif grid[y][x] == TREE and surroundings.count(LUMBERYARD) >= 3:
                new_grid[y][x] = LUMBERYARD
            elif grid[y][x] == LUMBERYARD:
                if not (surroundings.count(LUMBERYARD) >= 1) or not (surroundings.count(TREE) >= 1):
                    new_grid[y][x] = OPEN
    return new_grid

grid = copy.deepcopy(initial_grid)
for t in range(1, 11):
    grid = run_iteration(grid)

num_trees = sum([l.count(TREE) for l in grid])
num_lumberyards = sum([l.count(LUMBERYARD) for l in grid])

print("PART 1")
print(num_trees * num_lumberyards)

grid = copy.deepcopy(initial_grid)
grid_history = []
for t in itertools.count(1):
    grid = run_iteration(grid)
    if grid in grid_history:
        first_occurence = grid_history.index(grid)
        repeats_every = t - first_occurence - 1
        final_index = first_occurence + (1000000000 - first_occurence) % repeats_every - 1
        final_grid = grid_history[final_index]
        num_trees = sum([l.count(TREE) for l in final_grid])
        num_lumberyards = sum([l.count(LUMBERYARD) for l in final_grid])
        print("PART 2")
        print(num_trees * num_lumberyards)
        break
    grid_history.append(grid)

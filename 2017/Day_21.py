def diag(kp):
    nk = []
    for x in range(len(kp)):
        l = []
        for y in range(len(kp)):
            l.append(kp[y][x])
        nk.append("".join(l))
    return tuple(nk)


rules = {}
with open("input_21.txt") as file:
    for index, line in enumerate(file):
        condition, target = line.strip().split(" => ")
        
        condition = tuple(condition.split("/"))
        target = target.split("/")
        
        for variant in [condition, tuple([s[::-1] for s in condition]), tuple(s for s in condition[::-1]), tuple([s[::-1] for s in condition[::-1]])]:
            rules[variant] = target
            rules[diag(variant)] = target

def num_on(g):
    return sum([l.count("#") for l in g])


def run_iterations(num_iterations):
    grid = [
        ".#.",
        "..#",
        "###",
    ]
    
    for iter in range(num_iterations):
        newgrid = []

        pattern_size = 3
        if len(grid) % 2 == 0:
            pattern_size = 2
        
        for y in range(0, len(grid), pattern_size):
            newlines = [[] for _ in range(pattern_size + 1)]
            
            for x in range(0, len(grid), pattern_size):
                condition = []
                for i in range(pattern_size):
                    condition.append(grid[y + i][x:x + pattern_size])

                for j, l in enumerate(rules[tuple(condition)]):
                    newlines[j] += l

            newgrid.extend(["".join(l) for l in newlines])
        grid = newgrid

    return num_on(grid)

print("PART 1")
print(run_iterations(5))
print("PART 2")
print(run_iterations(18))

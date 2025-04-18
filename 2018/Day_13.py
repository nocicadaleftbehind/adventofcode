grid = []
with open("input_13.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        grid.append(list(line))


def turn_left(direction):
    return direction * -1j


def turn_right(direction):
    return direction * 1j


def turn(times, direction):
    if times == 0:
        return turn_left(direction)
    elif times == 2:
        return turn_right(direction)
    return direction


def grid_content(grid, pos):
    return grid[int(pos.imag)][int(pos.real)]

RIGHT = 1 + 0j
LEFT = -1 + 0j
UP = 0 - 1j
DOWN = 0 + 1j

carts = []
for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        if cell not in ["<", ">", "v", "^"]:
            continue

        if cell == ">" or cell == "<":
            grid[y][x] = "-"
        else:
            grid[y][x] = "|"

        cart_direction = {"^": UP, "v": DOWN, "<": LEFT, ">": RIGHT}[cell]
        new_cart = {"pos": x + y * 1j, "direction": cart_direction, "turn_no": 0, "dead": False}
        carts.append(new_cart)

first_crash = True
while len(carts) > 1:
    sorted_carts = sorted(carts, key=lambda c: (c["pos"].imag, -c["pos"].real))
    for cart in sorted_carts:
        if cart["dead"]:
            continue
        
        current_direction = cart["direction"]
        current_pos = cart["pos"] + current_direction
        cart["pos"] = current_pos

        if grid_content(grid, cart["pos"]) == "/":
            if current_direction == DOWN or current_direction == UP:
                current_direction = turn_right(current_direction)
            else:
                current_direction = turn_left(current_direction)

        if grid_content(grid, current_pos) == "\\":
            if current_direction == LEFT or current_direction == RIGHT:
                current_direction = turn_right(current_direction)
            else:
                current_direction = turn_left(current_direction)

        if grid_content(grid, current_pos) == "+":
            current_direction = turn(cart["turn_no"] % 3, current_direction)
            cart["turn_no"] += 1
        cart["direction"] = current_direction

        colls = [c for c in carts if c["pos"] == cart["pos"]]
        if len(colls) > 1:
            if first_crash:
                print("PART 1")
                print(f"{int(colls[0]['pos'].real)},{int(colls[0]['pos'].imag)}")
                first_crash = False

            for c in colls:
                c["dead"] = True

    carts = [c for c in carts if not c["dead"]]

print("PART 2")
print(f"{int(carts[0]['pos'].real)},{int(carts[0]['pos'].imag)}")

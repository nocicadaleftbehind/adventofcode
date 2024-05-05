import hashlib

hash_seed = open("input_17.txt").read().strip()
found_routes = []


def get_open_doors(route):
    digest = hash_seed + route
    hash = hashlib.md5(digest.encode()).hexdigest()
    open_doors_hash = hash[:4]
    open_doors = [direction for i, direction in enumerate("UDLR") if open_doors_hash[i] in "bcdef"]
    return open_doors


def valid_route(route):
    position = {"x": 1, "y": 4}
    for c in route:
        if c == "U":
            position["y"] += 1
        if c == "D":
            position["y"] -= 1
        if c == "R":
            position["x"] += 1
        if c == "L":
            position["x"] -= 1
        if position["x"] < 1 or position["x"] > 4:
            return False
        if position["y"] < 1 or position["y"] > 4:
            return False
        if position["x"] == 4 and position["y"] == 1:
            found_routes.append(route)
            return False
    return True


list_of_routes = [""]
while len(list_of_routes) > 0:
    route = list_of_routes.pop(0)
    for r in get_open_doors(route):
        next_route = route + r
        if valid_route(next_route):
            list_of_routes.append(next_route)

print("PART 1")
print(found_routes[0])
print("PART 2")
print(max([len(r) for r in found_routes]))

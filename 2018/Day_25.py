import itertools
from collections import defaultdict


def distance(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(4)])


coordinates = []
with open("input_25.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        coords = [int(x) for x in line.split(",")]
        coordinates.append(coords)

num_stars = len(coordinates)

neighbors = defaultdict(set)
for p1, p2 in itertools.product(range(num_stars), range(num_stars)):
    point1 = coordinates[p1]
    point2 = coordinates[p2]
    dist = distance(point1, point2)
    if dist <= 3:
        neighbors[p1].add(p2)

stars_not_yet_in_constellation = [i for i in range(num_stars)]
num_constellations = 0
while len(stars_not_yet_in_constellation) > 0:
    full_constellation = {stars_not_yet_in_constellation[0]}

    while True:
        change = False
        grown_constellation = {x for x in full_constellation}
        for star in full_constellation:
            for neighbor in neighbors[star]:
                change = True
                grown_constellation.add(neighbor)
            neighbors[star] = set()
        full_constellation = grown_constellation
        if not change:
            break

    for star in full_constellation:
        stars_not_yet_in_constellation.remove(star)
    num_constellations += 1

print("PART 1")
print(num_constellations)

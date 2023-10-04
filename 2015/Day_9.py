import math

import itertools

distances = {}
all_cities = []
with open("input_9.txt") as file:
    for line in file:
        city_1, temp_part = line.split(" to ")
        city_2, distance = temp_part.split(" = ")
        distance = int(distance[:-1])

        distances[(city_1, city_2)] = distance
        distances[(city_2, city_1)] = distance
        all_cities.append(city_1)
        all_cities.append(city_2)
all_cities = list(set(all_cities))

lowest_distance_yet = math.inf
highest_distance_yet = 0
for path in itertools.permutations(all_cities):
    total_distance = 0
    for i in range(len(path) - 1):
        a = path[i]
        b = path[i + 1]
        total_distance += distances[(a, b)]
        
    lowest_distance_yet = min(total_distance, lowest_distance_yet)
    highest_distance_yet = max(total_distance, highest_distance_yet)
print(lowest_distance_yet)
print(highest_distance_yet)

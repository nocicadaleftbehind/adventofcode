import re
from pprint import pprint


def sum_stat(cookie_stats, statname, n0, n1, n2, n3):
    ns = [n0, n1, n2, n3]
    summed_stat = sum([cookie_stats[i][statname] * ns[i] for i in range(4)])
    return max(summed_stat, 0)


cookie_stats = []
with open("input_15.txt") as file:
    for line in file:
        m = re.match("(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)",
                     line)
        if m:
            name = m.group(1)
            capacity = int(m.group(2))
            durability = int(m.group(3))
            flavor = int(m.group(4))
            texture = int(m.group(5))
            calories = int(m.group(6))
            cookie_stats.append({"name": name,
                                 "capacity": capacity,
                                 "durability": durability,
                                 "flavor": flavor,
                                 "texture": texture,
                                 "calories": calories})

best_points = 0
for n0 in range(100):
    for n1 in range(100 - n0):
        for n2 in range(100 - n1 - n0):
            n3 = 100 - n2 - n1 - n0
            capacity = sum_stat(cookie_stats, "capacity", n0, n1, n2, n3)
            durability = sum_stat(cookie_stats, "durability", n0, n1, n2, n3)
            flavor = sum_stat(cookie_stats, "flavor", n0, n1, n2, n3)
            texture = sum_stat(cookie_stats, "texture", n0, n1, n2, n3)
            
            calories = sum_stat(cookie_stats, "calories", n0, n1, n2, n3)
            if calories != 500:
                continue

            points = capacity * durability * flavor * texture

            best_points = max(best_points, points)


print(best_points)
import math
import re
from copy import copy

player_base = {
    "hp": 100,
    "attack": 0,
    "armor": 0
}

boss_base = {
    "hp": 0,
    "attack": 0,
    "armor": 0
}

with open("input_21.txt") as f:
    for line in f:
        if m:= re.match("Hit Points: (\d+)", line):
            boss_base["hp"] = int(m.group(1))
        if m:= re.match("Damage: (\d+)", line):
            boss_base["attack"] = int(m.group(1))
        if m:= re.match("Armor: (\d+)", line):
            boss_base["armor"] = int(m.group(1))
            
weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]


def sim_fight(player, boss):
    while True:
        player_damage = max(player["attack"] - boss["armor"], 1)
        boss["hp"] -= player_damage
        if boss["hp"] <= 0:
            return True
        boss_damage = max(boss["attack"] - player["armor"], 1)
        player["hp"] -= boss_damage
        if player["hp"] <= 0:
            return False


lowest_price = math.inf
highest_price = 0
for weapon in weapons:
    w_price, w_attack, w_armor = weapon
    for armor in armors:
        a_price, a_attack, a_armor = armor
        for ring_1 in rings:
            r_price, r_attack, r_armor = ring_1
            for ring_2 in rings:
                r2_price, r2_attack, r2_armor = ring_2
                if ring_1 == ring_2:
                    continue

                player = copy(player_base)
                player["attack"] += w_attack + a_attack + r_attack + r2_attack
                player["armor"] += w_armor + a_armor + r_armor + r2_armor
                gold = w_price + a_price + r_price + r2_price
                boss = copy(boss_base)

                result = sim_fight(player, boss)
                if result:
                    lowest_price = min(lowest_price, gold)
                else:
                    highest_price = max(highest_price, gold)

print("PART 1")
print(lowest_price)
print("PART 2")
print(highest_price)

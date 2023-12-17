from copy import copy
from heapq import heappush, heappop
import re

player_base = {
    "hp": 50,
    "armor": 0,
    "mana": 500,
    "shield_counter": 0,
    "recharge_counter": 0,
    "history": ""
}

boss_base = {
    "hp": 0,
    "attack": 0,
    "poison_counter": 0
}

with open("input_22.txt") as f:
    for line in f:
        if m:= re.match("Hit Points: (\d+)", line):
            boss_base["hp"] = int(m.group(1))
        if m:= re.match("Damage: (\d+)", line):
            boss_base["attack"] = int(m.group(1))


def turn(player, boss, spells):
    for spell in spells:
        # comment out for part 1
        player["hp"] -= 1
        
        if player["hp"] <= 0:
            return -1

        turn_upkeep(boss, player)

        if boss["hp"] <= 0:
            return 1
        if player["mana"] < 53:
            return -1

        cast_spell(player, boss, spell)

        if player["mana"] < 0:
            return -1
        if boss["hp"] <= 0:
            return 1

        turn_upkeep(boss, player)

        if boss["hp"] <= 0:
            return 1

        player["hp"] -= max(boss["attack"] - player["armor"], 1)
        if player["hp"] <= 0:
            return -1
    return 0


def cast_spell(player, boss, spell):
    player["history"] = player["history"] + spell
    if spell == "M":
        player["mana"] -= 53
        boss["hp"] -= 4
    elif spell == "D":
        player["mana"] -= 73
        boss["hp"] -= 2
        player["hp"] += 2
    elif spell == "S":
        player["mana"] -= 113
        player["shield_counter"] = 6
    elif spell == "P":
        player["mana"] -= 173
        boss["poison_counter"] = 6
    elif spell == "R":
        player["mana"] -= 229
        player["recharge_counter"] = 5


def turn_upkeep(boss, player):
    if player["shield_counter"] > 0:
        player["armor"] = 7
        player["shield_counter"] -= 1
    else:
        player["armor"] = 0

    if player["recharge_counter"] > 0:
        player["mana"] += 101
        player["recharge_counter"] -= 1

    if boss["poison_counter"] > 0:
        boss["hp"] -= 3
        boss["poison_counter"] -= 1

spell_costs = [(53, "M"), (73, "D"), (113, "S"), (173, "P"), (229, "R")]
spell_queue = []
heappush(spell_queue, (0, ""))
while True:
    min_mana, spells = heappop(spell_queue)
    player = copy(player_base)
    boss = copy(boss_base)
    winning = turn(player, boss, spells)
    if winning == 1:
        print(min_mana)
        break
    elif winning == 0:
        for mana, spell in spell_costs:
            new_item = (min_mana + mana, spells + spell)
            heappush(spell_queue, new_item)

import copy
import itertools
import re

IMMUNE_SYSTEM = 1
INFECTION = 2


class UnitGroup:
    def __init__(self, m, current_id, current_team):
        self.id = current_id
        self.team = current_team
        self.number = int(m.group(1))
        self.hp = int(m.group(2))
        self.weaknesses, self.immunities = parse_immunities(m.group(3))
        self.damage = int(m.group(4))
        self.attack_type = m.group(5)
        self.initiative = int(m.group(6))


def parse_immunities(s):
    weak_list = []
    match = re.search("weak to ([^;^\)]*)", s)
    if match:
        weak_list = [e.strip() for e in match.group(1).split(",")]

    immune_list = []
    match = re.search("immune to ([^;^\)]*)", s)
    if match:
        immune_list = [e.strip() for e in match.group(1).split(",")]

    return weak_list, immune_list


def rank_targets(current_bot, bots):
    bots = [bot for bot in bots if
            damage_adjusted(current_bot, bot) > 0 and bot.number > 0 and current_bot.team != bot.team]
    bots.sort(key=lambda x: (damage_adjusted(current_bot, x), power(x), x.initiative), reverse=True)

    return [bot.id for bot in bots]


def take_damage(current_bot, dmg):
    n = min(dmg // current_bot.hp, current_bot.number)
    current_bot.number -= n
    return n


def fight(current_bot, target):
    damage = damage_adjusted(current_bot, target)
    return take_damage(target, damage)


def damage_adjusted(current_bot, enemy_bot):
    damage = power(current_bot)

    if current_bot.attack_type in enemy_bot.weaknesses:
        damage *= 2
    if current_bot.attack_type in enemy_bot.immunities:
        damage = 0
    return damage


def power(bot):
    return bot.number * bot.damage


def _get_bot_by_id(bots, target_id):
    return [bot for bot in bots if bot.id == target_id][0]


def target_selection(bots):
    targets = {}
    bots.sort(key=lambda x: (power(x), x.initiative), reverse=True)

    for current_bot in bots:
        ranked_enemies = rank_targets(current_bot, bots)

        for target_id in ranked_enemies:
            if target_id in targets.values():
                continue

            targets[current_bot.id] = target_id
            break

    return targets


def fight_round(bots):
    targets = target_selection(bots)

    kills = 0
    for current_bot in sorted(bots, key=lambda x: x.initiative, reverse=True):
        if current_bot.id not in targets.keys():
            continue

        target = _get_bot_by_id(bots, targets[current_bot.id])
        kills += fight(current_bot, target)
    return kills


def simulate(bots, boost=0):
    bots = copy.deepcopy(bots)
    for bot in bots:
        if bot.team == IMMUNE_SYSTEM:
            bot.damage += boost

    while True:
        teams = [bot.team for bot in bots]
        if len(set(teams)) <= 1:
            winner = teams[0]
            break

        num_kills = fight_round(bots)
        if num_kills == 0:
            winner = 0
            break

        bots = [bot for bot in bots if bot.number > 0]
    number_survivors = sum([bot.number for bot in bots if bot.number > 0])

    return winner == IMMUNE_SYSTEM, number_survivors


bots = []
with open("input_24.txt") as file:
    current_team = None
    current_id = 1
    for line in file:
        line = line.replace("\n", "")
        if line == "Immune System:":
            current_team = IMMUNE_SYSTEM
        elif line == "Infection:":
            current_team = INFECTION
        pattern = r"(\d+) units each with (\d+) hit points(.*) with an attack that does (\d+) (.*) damage at initiative (\d+)"
        m = re.search(pattern, line)
        if m:
            bot = UnitGroup(m, current_id, current_team)
            current_id += 1
            bots.append(bot)

for boost in itertools.count(0):
    end, num_surviving = simulate(bots, boost)
    if boost == 0:
        print("PART 1")
        print(num_surviving)
    if end:
        print("PART 2")
        print(num_surviving)
        break

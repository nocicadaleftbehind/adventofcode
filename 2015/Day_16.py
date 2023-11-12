import re


def match_stat(line, regex):
    m = re.search(regex, line)
    if m:
        return int(m.group(1))
    else:
        return "?"


aunt_attributes = []
with open("input_16.txt") as file:
    for line in file:
        sue_number = match_stat(line, "Sue (\d+)")
        children = match_stat(line, "children: (\d+)")
        cats = match_stat(line, "cats: (\d+)")
        samoyeds = match_stat(line, "samoyeds: (\d+)")
        pomeranians = match_stat(line, "pomeranians: (\d+)")
        akitas = match_stat(line, "akitas: (\d+)")
        vizlas = match_stat(line, "vizslas: (\d+)")
        goldfish = match_stat(line, "goldfish: (\d+)")
        trees = match_stat(line, "trees: (\d+)")
        cars = match_stat(line, "cars: (\d+)")
        perfumes = match_stat(line, "perfumes: (\d+)")
        aunt_attributes.append({
            "number": sue_number,
            "children": children,
            "cats": cats,
            "samoyeds": samoyeds,
            "pomeranians": pomeranians,
            "akitas": akitas,
            "vizslas": vizlas,
            "goldfish": goldfish,
            "trees": trees,
            "cars": cars,
            "perfumes": perfumes
        })

clues = {"children": 3,
         "cats": 7,
         "samoyeds": 2,
         "pomeranians": 3,
         "akitas": 0,
         "vizslas": 0,
         "goldfish": 5,
         "trees": 3,
         "cars": 2,
         "perfumes": 1}


def invalid_attr(aunt, attr):
    value = aunt[attr]
    clue = clues[attr]
    if attr == "cats" or attr == "trees":
        return_value = value == "?" or value >= clue
    elif attr == "pomeranians" or attr == "goldfish":
        return_value = value == "?" or value <= clue
    else:
        return_value = value == "?" or value == clue
    return return_value


for aunt in aunt_attributes:
    valid = True
    for attr in clues.keys():
        if not valid:
            continue
        valid = valid and invalid_attr(aunt, attr)
    if valid:
        print(aunt["number"])

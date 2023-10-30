import re
from itertools import permutations

happiness_gains = {}
people = []

with open("input_13.txt") as file:
    for line in file:
        m = re.match("(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", line)
        if m:
            person1 = m.group(1)
            sign = m.group(2)
            amount = m.group(3)
            person2 = m.group(4)

            amount = int(amount)
            people = list(set(people + [person1, person2]))
            if sign == "lose":
                amount *= -1

            happiness_gains[(person1, person2)] = amount


def brute_force_search(people, happiness_gains):
    highest_happiness_yet = 0
    for path in permutations(people):
        total_happiness = happiness_gains[path[0], path[-1]]
        total_happiness += happiness_gains[path[-1], path[0]]
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            total_happiness += happiness_gains[(a, b)]
            total_happiness += happiness_gains[(b, a)]
        if total_happiness > highest_happiness_yet:
            highest_happiness_yet = max(total_happiness, highest_happiness_yet)
    return highest_happiness_yet


print("Part 1")
print(brute_force_search(people, happiness_gains))

for p in people:
    happiness_gains[(p, "You")] = 0
    happiness_gains[("You", p)] = 0
people.append("You")

print("Part 2")
print(brute_force_search(people, happiness_gains))

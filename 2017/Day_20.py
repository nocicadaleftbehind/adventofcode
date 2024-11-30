import copy
import re

particles = []
with open("input_20.txt") as file:
    for index, line in enumerate(file):
        m = re.match("p=<(.+),(.+),(.+)>, v=<(.+),(.+),(.+)>, a=<(.+),(.+),(.+)>", line)

        positions = list(map(int, [m.group(i) for i in range(1, 10)]))

        particle = {
            "alive": True,
            "i": index,
            "p": [positions[0], positions[1], positions[2]],
            "v": [positions[3], positions[4], positions[5]],
            "a": [positions[6], positions[7], positions[8]]
        }
        particles.append(particle)


def check_collusions(particles):
    for particle in particles:
        for other_particle in particles:
            if particle["i"] <= other_particle["i"]:
                continue

            same_positions = [particle["p"][i] == other_particle["p"][i] for i in range(3)]
            if all(same_positions):
                particle["alive"] = False
                other_particle["alive"] = False


def simulate(particles):
    for particle in particles:
        for i in range(3):
            particle["v"][i] += particle["a"][i]
            particle["p"][i] += particle["v"][i]


def diff_to_zero(p1):
    return sum((abs(p1[i]) for i in range(3)))


def run_simulation(particles, collusion):
    last_score = None
    num_stable = 0
    while True:
        simulate(particles)
        if collusion:
            check_collusions(particles)
            particles = [p for p in particles if p["alive"]]
            score = len(particles)
        else:
            distances = [(diff_to_zero(p["p"]), p["i"]) for p in particles]
            score = list(sorted(distances))[0][1]

        if last_score != score:
            last_score = score
            num_stable = 0
        else:
            num_stable += 1

        if num_stable > 500:
            return last_score


print("PART 1")
print(run_simulation(copy.deepcopy(particles), collusion=False))
print("PART 2")
print(run_simulation(copy.deepcopy(particles), collusion=True))

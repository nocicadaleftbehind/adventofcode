import re
from pprint import pprint


def race_distance(fly_speed, fly_duration, rest_duration, race_length):
    distance = 0
    num_periods = int(race_length / (fly_duration + rest_duration))
    distance += num_periods * fly_speed * fly_duration
    race_length -= num_periods * (fly_duration + rest_duration)
    race_length = min(race_length, fly_duration)
    distance += fly_speed * race_length
    return distance

total_race_duration = 2503
reindeer_stats = []
best_distance = 0
with open("input_14.txt") as file:
    for line in file:
        m = re.match("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
        if m:
            name = m.group(1)
            fly_speed = int(m.group(2))
            fly_duration = int(m.group(3))
            rest_duration = int(m.group(4))
            reindeer_stats.append({"name": name,
                                   "fly_speed": fly_speed,
                                   "fly_duration": fly_duration,
                                   "rest_duration": rest_duration,
                                   "points": 0,
                                   "status": "flying",
                                   "distance": 0,
                                   "since": 0})

            distance = race_distance(fly_speed, fly_duration, rest_duration, total_race_duration)
            best_distance = max(best_distance, distance)
print("Part 1", best_distance)

for i in range(total_race_duration):
    for reindeer in reindeer_stats:
        reindeer["since"] += 1
        
        if reindeer["status"] == "flying":
            reindeer["distance"] += reindeer["fly_speed"]
            if reindeer["since"] >= reindeer["fly_duration"]:
                reindeer["since"] = 0
                reindeer["status"] = "resting"
        else:
            if reindeer["since"] >= reindeer["rest_duration"]:
                reindeer["since"] = 0
                reindeer["status"] = "flying"

    best_reindeers = sorted(reindeer_stats, key=lambda x: x["distance"], reverse=True)
    best_distance = best_reindeers[0]["distance"]
    first_place = [x for x in best_reindeers if x["distance"] == best_distance]
    
    for r in first_place:
        r["points"] += 1

best_reindeer = list(sorted(reindeer_stats, key=lambda x: x["points"], reverse=True))[0]
print("Part 2", best_reindeer["points"])
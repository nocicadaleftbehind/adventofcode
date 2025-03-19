import re
from collections import deque

input_line = open("input_9.txt").read()
m = re.match("(\d+) players; last marble is worth (\d+) points", input_line)
num_players = int(m.group(1))
last_marble = int(m.group(2))


def run_game(last_marble):
    current_player = 0
    points = [0] * num_players
    marble_circle = deque([0])
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            marble_circle.rotate(7)
            points[current_player] += marble + marble_circle.pop()
            marble_circle.rotate(-1)
        else:
            marble_circle.rotate(-1)
            marble_circle.append(marble)
        current_player = (current_player + 1) % num_players
    return max(points)


print("PART 1")
print(run_game(last_marble))
print("PART 2")
print(run_game(last_marble * 100))

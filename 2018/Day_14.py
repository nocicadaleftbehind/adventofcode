import itertools

pattern = open("input_14.txt").read()
target_length = int(pattern)

scoreboard = "37"
pos_1 = 0
pos_2 = 1
for i in itertools.count(1):
    if len(scoreboard) == target_length + 12:
        print("PART 1")
        print(scoreboard[target_length: target_length+10])
    if pattern in scoreboard[-len(pattern)-1:]:
        print("PART 2")
        print(len(scoreboard) - 7)
        break
    scoreboard += str(int(scoreboard[pos_1]) + int(scoreboard[pos_2]))
    pos_1 = (1 + pos_1 + int(scoreboard[pos_1])) % len(scoreboard)
    pos_2 = (1 + pos_2 + int(scoreboard[pos_2])) % len(scoreboard)

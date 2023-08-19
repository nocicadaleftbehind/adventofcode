def move(movelist, num_santas):
    visited_pos = {0}
    
    for i in range(num_santas):
        specific_move_list = movelist[i::num_santas]    
        pos = 0 + 0j
        for char in specific_move_list:
            next_move = {"^": 1j, "v": -1j, "<": -1, ">": 1}[char]
            pos += next_move
            visited_pos.add(pos)
    
    return len(visited_pos)

print("PART 1")
print(move(">", 1))
print(move("^>v<", 1))
print(move("^v^v^v^v^v", 1))
print(move(open("input_3.txt").read(), 1))

print("PART 2")
print(move("^v", 2))
print(move("^>v<", 2))
print(move("^v^v^v^v^v", 2))
print(move(open("input_3.txt").read(), 2))

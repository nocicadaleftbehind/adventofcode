import numpy as np


def split_coordinates(string):
    split = string.split(",")
    return int(split[0]), int(split[1])

def handle_instruction(grid, instruction, start_x, start_y, end_x, end_y):
    if instruction == "turnon":
        grid[start_x:end_x+1, start_y:end_y+1] = 1
    if instruction == "turnoff":
        grid[start_x:end_x+1, start_y:end_y+1] = 0
    if instruction == "toggle":
        grid[start_x:end_x+1, start_y:end_y+1] = 1 - grid[start_x:end_x+1, start_y:end_y+1]
    return grid

def handle_instruction_2(grid, instruction, start_x, start_y, end_x, end_y):
    if instruction == "turnon":
        grid[start_x:end_x+1, start_y:end_y+1] += 1
    if instruction == "turnoff":
        grid[start_x:end_x+1, start_y:end_y+1] -= 1
        grid = grid.clip(0)
    if instruction == "toggle":
        grid[start_x:end_x+1, start_y:end_y+1] += 2
    return grid


grid = np.zeros((1000, 1000))
with open("input_6.txt") as file:
    for line in file:
        parts = line.split(" through ")
        subparts = parts[0].split(" ")
        start_x, start_y = split_coordinates(subparts[-1])
        end_x, end_y = split_coordinates(parts[1])
        instruction = "".join(subparts[:-1])
        grid = handle_instruction(grid, instruction, start_x, start_y, end_x, end_y)
print(np.sum(grid))
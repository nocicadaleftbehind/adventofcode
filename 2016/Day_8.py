import re

import numpy


def turn_on(w, l):
    field[0:l, 0:w] = True


def rotate_row(index, amount):
    field[index, :] = numpy.roll(field[index, :], amount)


def rotate_column(index, amount):
    field[:, index] = numpy.roll(field[:, index], amount)


WIDTH = 50
HEIGHT = 6
field = numpy.zeros([HEIGHT, WIDTH], dtype=numpy.bool_)

with open("input_8.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("rect (.+)x(.+)", line)
        if m:
            width = int(m.group(1))
            height = int(m.group(2))
            turn_on(width, height)
        m = re.match("rotate column x=(.+) by (.+)", line)
        if m:
            column = int(m.group(1))
            amount = int(m.group(2))
            rotate_column(column, amount)
        m = re.match("rotate row y=(.+) by (.+)", line)
        if m:
            row = int(m.group(1))
            amount = int(m.group(2))
            rotate_row(row, amount)

print("PART 1")
print(field.sum())


def print_matrix(matrix):
    for j in range(HEIGHT):
        s = ""
        for i, c in enumerate(matrix[j, :]):
            if i % 5 == 0:
                s += "  "
            if c > 0:
                s += "X"
            else:
                s += " "
        print(s)


print("PART 2")
print_matrix(field)

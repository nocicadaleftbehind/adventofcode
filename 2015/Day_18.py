import numpy as np

FIELD_SIZE = 100
field = np.zeros((FIELD_SIZE + 2, FIELD_SIZE + 2), dtype=np.int8)
with open("input_18.txt") as file:
    for lineno, line in enumerate(file):
        line = line[:-1]
        line = line.replace(".", "0")
        line = line.replace("#", "1")
        chararray = list(line)
        chararray = [int(x) for x in chararray]
        field[lineno+1, 1:-1] = chararray

def part_1(field):
    for stepno in range(100):
        new_field = np.zeros((FIELD_SIZE + 2, FIELD_SIZE + 2), dtype=np.int8)
    
        for x in range(1, FIELD_SIZE + 1):
            for y in range(1, FIELD_SIZE + 1):
                current = field[x,y]
                numneighbors = field[x-1:x+2,y-1:y+2].sum() - current
                if current == 1:
                    if numneighbors in [2,3]:
                        new_field[x, y] = 1
                    else:
                        new_field[x, y] = 0
                if current == 0:
                    if numneighbors == 3:
                        new_field[x, y] = 1
                    else:
                        new_field[x, y] = 0
        field = new_field
    return field.sum()


def part_2(field):
    field[1,FIELD_SIZE] = 1
    field[FIELD_SIZE,FIELD_SIZE] = 1
    field[1,1] = 1
    field[FIELD_SIZE,1] = 1
    
    for stepno in range(100):
        new_field = np.zeros((FIELD_SIZE + 2, FIELD_SIZE + 2), dtype=np.int8)

        for x in range(1, FIELD_SIZE + 1):
            for y in range(1, FIELD_SIZE + 1):
                if (x == 1 and y == 1) or (x == 1 and y == FIELD_SIZE) or (x == FIELD_SIZE and y == 1) or (x == FIELD_SIZE and y == FIELD_SIZE):
                    new_field[x,y] = 1
                    continue
                current = field[x, y]
                numneighbors = field[x - 1:x + 2, y - 1:y + 2].sum() - current
                if current == 1:
                    if numneighbors in [2, 3]:
                        new_field[x, y] = 1
                    else:
                        new_field[x, y] = 0
                if current == 0:
                    if numneighbors == 3:
                        new_field[x, y] = 1
                    else:
                        new_field[x, y] = 0
        field = new_field
    return field.sum()

print(part_1(np.copy(field)))
print(part_2(np.copy(field)))
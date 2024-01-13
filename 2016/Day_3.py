lines = []
with open("input_3.txt") as file:
    for line in file:
        sides = list(map(int, [s for s in line.strip().split(" ") if s != " " and s != ""]))
        lines.append((sides[0], sides[1], sides[2]))

def is_triangle(side_1, side_2, side_3):
    if side_1 >= side_2 + side_3:
        return False
    if side_2 >= side_1 + side_3:
        return False
    if side_3 >= side_1 + side_2:
        return False
    return True

num_triangles = 0
for triangle in lines:
    if is_triangle(triangle[0], triangle[1], triangle[2]):
        num_triangles += 1
print("PART 1")
print(num_triangles)

num_triangles = 0
for i in range(len(lines) // 3):
    for col in range(3):
        if is_triangle(lines[3*i][col], lines[3*i+1][col], lines[3*i+2][col]):
            num_triangles += 1
print("PART 2")
print(num_triangles)

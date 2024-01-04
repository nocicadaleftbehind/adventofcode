import re

line = open("input_25.txt").read()
m = re.match(r".* row (\d+), column (\d+)", line)
if m:
    row = int(m.group(1))
    column = int(m.group(2))

completed_diagonal = row + column - 2
number_iterations = (completed_diagonal ** 2 + completed_diagonal) // 2 + column

x = 20151125
for i in range(2, number_iterations+1):
    x = (x * 252533) % 33554393
print(x)

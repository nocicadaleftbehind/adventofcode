import re

lines = []
with open("input_7.txt") as file:
    for line in file:
        lines.append(line.strip())

def part_1(lines):
    def contains_abba(group):
        if matches := re.findall(r"(.)(.)\2\1", group):
            for m in matches: 
                if m[0] != m[1]:
                    return True
        return False
    
    valid_lines = 0
    for line in lines:
        groups = re.split("[\[\]]", line)
        if any([contains_abba(g) for g in groups[::2]]) and all([not contains_abba(g) for g in groups[1::2]]):
            valid_lines += 1
        
    return valid_lines

def part_2(lines):
    valid_lines = 0
    for line in lines:
        groups = re.split("[\[\]]", line)
        valid_line = False
        for group in groups[::2]:
            tuples = zip(group, group[1:], group[2:])
            abas = [b + a + b for a, b, c in tuples if a == c and a != b]
            for aba in abas:
                if re.search(f"\[[^\]]*{aba}[^\]]*\]", line):
                    valid_line = True
        if valid_line:
            valid_lines += 1
    return valid_lines

print("PART 1")
print(part_1(lines))
print("PART 2")
print(part_2(lines))
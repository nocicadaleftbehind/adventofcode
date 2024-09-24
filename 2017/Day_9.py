with open("input_9.txt") as file:
    s = file.read()[:-1]


def calc_score(s):
    in_garbage = False
    skip_next_char = False
    
    depth = 0
    depth_score = 0
    
    garbage_count = 0
    for char in s:
        if skip_next_char:
            skip_next_char = False
            continue
        if in_garbage:
            if char == ">":
                in_garbage = False
            elif char == "!":
                skip_next_char = True
            else:
                garbage_count += 1
        else:
            if char == "{":
                depth += 1
            elif char == "}":
                depth_score += depth
                depth -= 1
            elif char == "<":
                in_garbage = True
    return depth_score, garbage_count

depth_score, garbage_count = calc_score(s)
print("PART 1")
print(depth_score)
print("PART 2")
print(garbage_count)

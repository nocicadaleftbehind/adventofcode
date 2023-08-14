input_string = open("input_2.txt").readlines()

def wrapping_area(dimensions_line):
    l, w, h = dimensions_line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    area = 2 * l * w + 2 * w * h + 2 * l * h + min(l * w, w * h, l * h)
    return area

def wrapping_area_loop(packet_list):
    total_area = 0
    for line in packet_list:
        total_area += wrapping_area(line)
    return total_area

def ribbon_length(dimensions_line):
    l, w, h = dimensions_line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    ribbon = 2 * (l + w + h - max(l, w, h))
    ribbon += l * w * h
    return ribbon

def ribbon_length_loop(packet_list):
    total_length = 0
    for line in packet_list:
        total_length += ribbon_length(line)
    return total_length

print("PART 1")
print(wrapping_area("2x3x4"))
print(wrapping_area("1x1x10"))
print(wrapping_area_loop(input_string))

print("PART 2")
print(ribbon_length("2x3x4"))
print(ribbon_length("1x1x10"))
print(ribbon_length_loop(input_string))
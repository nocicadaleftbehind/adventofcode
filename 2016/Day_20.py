import re

ranges = []

with open("input_20.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("(\d+)-(\d+)", line)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            ranges.append((start, end))


def get_allowed_ips(ranges):
    ranges.sort()
    range_index = 0

    allowed_ips = []

    ip = 0
    while ip < 2 ** 32:
        lower, upper = ranges[range_index]
        if ip >= lower:
            if ip <= upper:
                ip = upper + 1
                continue
            range_index += 1
        else:
            allowed_ips.append(ip)
            ip += 1
    return allowed_ips


allowed_ips = get_allowed_ips(ranges)
print("PART 1")
print(allowed_ips[0])
print("PART 2")
print(len(allowed_ips))

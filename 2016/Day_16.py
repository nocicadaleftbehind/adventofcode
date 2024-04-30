start_state = open("input_16.txt").read()

def transform(s):
    a = s
    b = s.translate(str.maketrans("01", "10"))
    b = "".join(reversed(b))
    return a + "0" + b


def checksum(s):
    s_new = ""
    for a, b in zip(s[::2], s[1::2]):
        if a == b:
            s_new += "1"
        else:
            s_new += "0"
    return s_new

def recursive_checksum(s):
    while len(s) % 2 == 0:
        s = checksum(s)
    return s

def fill_state(target_length):
    s = start_state
    while True:
        s = transform(s)
        if len(s) >= target_length:
            s = s[:target_length]
            break

    return recursive_checksum(s)


print("PART 1")
print(fill_state(272))
print("PART 2")
print(fill_state(35651584))

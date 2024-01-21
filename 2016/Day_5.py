import hashlib
from itertools import count

initial_password = open("input_5.txt").read().strip()

def part_1():
    password = ""
    for i in count(0):
        string = initial_password + str(i)
        m = hashlib.md5(string.encode())
        hash = m.hexdigest()
        if hash[:5].startswith("00000"):
            password += hash[5]
        if len(password) == 8:
            return password

def part_2():
    password = list("-" * 8)
    for i in count(0):
        string = initial_password + str(i)
        m = hashlib.md5(string.encode())
        hash = m.hexdigest()
        if hash[:5] == "0" * 5:
            pos = hash[5]
            value = hash[6]
            if pos.isdigit() and int(pos) < 8:
                pos = int(pos)
                if password[pos] == "-":
                    password[pos] = value
        if "-" not in password:
            return "".join(password)

print("PART 1")
print(part_1())
print("PART 2")
print(part_2())

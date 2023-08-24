import hashlib
from itertools import count

def mine_adventcoin(prefix, needed_zeroes):
    for i in count(0):
        string = prefix + str(i)
        string = string.encode()
        hash = hashlib.md5(string).hexdigest()
        if hash[0:needed_zeroes] == "0" * needed_zeroes:
            return i

print("PART 1")
print(mine_adventcoin("abcdef", 5))
print(mine_adventcoin("pqrstuv", 5))
print(mine_adventcoin(open("input_4.txt").read(), 5))
print("PART 2")
print(mine_adventcoin(open("input_4.txt").read(), 6))

for i in range(8):
    print(mine_adventcoin(open("input_4.txt").read(), i))

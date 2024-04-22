import hashlib
import itertools
import re

salt = open("input_14.txt").read().strip()

hashdict = dict()


def check_if_three_repeats(hash):
    return re.findall("(.)\\1\\1", hash)


def check_if_five_repeats(i, character, num_rounds):
    for j in range(i + 1, i + 1001):
        hash = create_hash(j, num_rounds)
        if character * 5 in hash:
            return True
    return False


def create_hash(i, num_rounds):
    if i in hashdict.keys():
        return hashdict[i]
    hash = salt + str(i)
    for k in range(num_rounds):
        hash = hashlib.md5(hash.encode()).hexdigest()
    hashdict[i] = hash
    return hash


def find_keys(num_rounds):
    global hashdict
    hashdict = dict()
    found_keys = 0
    for i in itertools.count(0):
        hash = create_hash(i, num_rounds)
        repeating_chars = check_if_three_repeats(hash)
        for repeating_char in repeating_chars[:1]:
            if check_if_five_repeats(i, repeating_char, num_rounds):
                found_keys += 1
                if found_keys == 64:
                    return i


print("PART 1")
print(find_keys(1))

print("PART 2")
print(find_keys(2017))

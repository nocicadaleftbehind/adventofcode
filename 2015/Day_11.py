import re
from string import ascii_lowercase

input = open("input_11.txt").read()

def increment_string(string, pos=1):
    char_to_increment = string[-pos]
    if char_to_increment == "z":
        string[-pos] = "a"
        return increment_string(string, pos + 1)
    else:
        string[-pos] = chr(ord(char_to_increment) + 1)
        return string

def three_increasing_letters(string):
    for c in ascii_lowercase:
        pattern = c + chr(ord(c) + 1) + chr(ord(c) + 2)
        if pattern in string:
            return True
    return False

current = list(input)
num_solutions = 0
while True:
    current = increment_string(current)
    string = "".join(current)

    #Rule 1
    if not three_increasing_letters(string):
        continue
        
    #Rule 2
    if "i" in string or "o" in string or "l" in string:
        continue
    
    #Rule 3
    if not re.search("(.)\\1.+(.)\\2", string):
        continue

    num_solutions += 1
    print(string)
    if num_solutions == 2:
        break

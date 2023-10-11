import tqdm

input = open("input_10.txt").read()
num_repeats = 40


def look_and_say(string):
    new_string = ""
    num_repeats = 0
    old_char = string[0]
    for char in string:
        if char == old_char:
            num_repeats += 1
        else:
            new_string += str(num_repeats) + old_char
            old_char = char
            num_repeats = 1
    new_string += str(num_repeats) + old_char
    return new_string


for i in tqdm.tqdm(range(num_repeats)):
    input = look_and_say(input)

print(len(input))
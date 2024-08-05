input_string = open("input_1.txt").read()

def filter_duplicates(string, lookahead_string):
    filtered_string = [char for char, comp in zip(string, lookahead_string) if char == comp]
    return filtered_string


def sum_duplicates(string, lookahead):
    lookahead_string = (string + string)[lookahead:len(string) + lookahead]
    return sum([int(char) for char in filter_duplicates(string, lookahead_string)])


print("PART 1")
print(sum_duplicates(input_string, 1))
print("PART 2")
print(sum_duplicates(input_string, len(input_string) // 2))

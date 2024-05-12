first_row = open("input_18.txt").read().strip()

def generate_next_row(row):
    new_row = ""
    for i in range(1, len(row) - 1):
        char = "."
        if row[i-1:i+2] in ["^^.", ".^^", "..^", "^.."]:
            char = "^"
        new_row += char
    return new_row

def count_safe_fields(num_rows):
    last_row = first_row
    num_safe_fields = last_row.count(".")
    for i in range(num_rows - 1):
        new_row = generate_next_row("." + last_row + ".")
        num_safe_fields += new_row.count(".")
        last_row = new_row
    return num_safe_fields

print("PART 1")
print(count_safe_fields(40))
print("PART 2")
print(count_safe_fields(400000))

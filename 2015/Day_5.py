import re
import string


def has_three_vowels(string_to_check):
    if re.search("[aeiou].*[aeiou].*[aeiou].*", string_to_check):
        return True
    return False


def has_double_letters(string_to_check):
    if re.search("(.)\\1", string_to_check):
        return True
    return False


def no_forbidden_substring(string_to_check):
    if re.search("(ab)|(cd)|(pq)|(xy)", string_to_check):
        return False
    return True

def has_two_letter_pairs(string_to_check):
    if re.search("(..).*\\1", string_to_check):
        return True
    return False


def has_two_letter_seperated_by_one(string_to_check):
    if re.search("(.).\\1", string_to_check):
        return True
    return False

def nice_or_naughty(string_to_check):
    if (has_three_vowels(string_to_check)
            and has_double_letters(string_to_check)
            and no_forbidden_substring(string_to_check)):
        return True
    return False

def nice_or_naughty_2(string_to_check):
    if (has_two_letter_pairs(string_to_check)
            and has_two_letter_seperated_by_one(string_to_check)):
        return True
    return False

print("Part 1")
print(nice_or_naughty("ugknbfddgicrmopn"))
print(nice_or_naughty("aaa"))
print(nice_or_naughty("jchzalrnumimnmhp"))
print(nice_or_naughty("haegwjzuvuyypxyu"))
print(nice_or_naughty("dvszwmarrgswjxmb"))

print("Part 2")
print(nice_or_naughty_2("qjhvhtzxzqqjkmpb"))
print(nice_or_naughty_2("xxyxx"))
print(nice_or_naughty_2("uurcxstgmygtbstg"))
print(nice_or_naughty_2("ieodomkazucvgmuy"))

print("My Input")
num_nice_strings_1 = 0
num_nice_strings_2 = 0
with open("input_5.txt") as file:
    for line in file:
        if nice_or_naughty(line):
            num_nice_strings_1 += 1
        if nice_or_naughty_2(line):
            num_nice_strings_2 += 1

print(num_nice_strings_1)
print(num_nice_strings_2)

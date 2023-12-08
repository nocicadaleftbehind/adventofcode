import numpy

input = int(open("input_20.txt").read())


def part_1():
    num_presents = numpy.zeros((input // 10,))
    for elfnum in range(1, input // 10):
        num_presents[elfnum:(input // 10):elfnum] += elfnum * 10

    for house, num_present in enumerate(num_presents):
        if num_present >= input:
            return house


def part_2():
    num_presents = numpy.zeros((input // 11,))
    for elfnum in range(1, input // 11):
        num_presents[elfnum:50 * elfnum:elfnum] += elfnum * 11

    for house, num_present in enumerate(num_presents):
        if num_present >= input:
            return house


print("PART 1")
print(part_1())

print("PART 2")
print(part_2())

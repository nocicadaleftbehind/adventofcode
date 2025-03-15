nodes = []
with open("input_8.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        nodes = list(map(int, line.split(" ")))

class Node:
    def __init__(self):
        self.children = []
        self.data = []


def parse(data, node):
    num_children = data[0]
    num_meta_data = data[1]
    offset = 2
    for i in range(num_children):
        node.children.append(Node())
        offset += parse(data[offset:], node.children[i])
    for j in range(num_meta_data):
        node.data.append(data[offset + j])
    offset += num_meta_data
    return offset

def meta_data_sum(node):
    partial_sum = sum(node.data)
    for child in node.children:
        partial_sum += meta_data_sum(child)
    return partial_sum

def value(node):
    if len(node.children) == 0:
        return sum(node.data)
    partial_sum = 0
    for index in node.data:
        if index - 1 < len(node.children):
            partial_sum += value(node.children[index - 1])
    return partial_sum

head = Node()
parse(nodes, head)
print("PART 1")
print(meta_data_sum(head))
print("PART 2")
print(value(head))

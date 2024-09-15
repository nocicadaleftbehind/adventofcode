import re
from collections import Counter

tree = {}
weights = {}
with open("input_7.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("(.+) \((.+)\)( -> (.+))?", line)
        if m:
            name = m.group(1)
            weight = m.group(2)
            
            children = []
            children_list = line.split("->")
            if len(children_list) > 1:
                children_list = children_list[-1]
                children_list = children_list.split(",")
                children = [c.strip() for c in children_list]
            tree[name] = children
            weights[name] = int(weight)

def get_root(tree):
    root_name = list(tree.keys())[0]
    while True:
        new_root = root_name
        for name in tree.keys():
            if new_root in tree[name]:
                new_root = name
                break
        if new_root == root_name:
            return root_name
        root_name = new_root
        
def get_weight(node):
    total = weights[node]
    for child in tree[node]:
        total += get_weight(child)
    return total

def index_of_different(l):
    c = Counter(l)
    for v, count in c.items():
        if count == 1:
            return l.index(v)

def balance_tree(root):
    node = root
    diff = 0
    while True:
        child_nodes = tree[node]
        node_weights = [get_weight(child) for child in child_nodes]
        
        if len(set(node_weights)) == 1:
            return weights[node] - diff
        i = index_of_different(node_weights)
        node = child_nodes[i]
        if i == 0:
            diff = get_weight(child_nodes[i]) - get_weight(child_nodes[1])
        else:
            diff = get_weight(child_nodes[i]) - get_weight(child_nodes[0])

print("PART 1")
root = get_root(tree)
print(root)
print("PART 2")
print(balance_tree(root))

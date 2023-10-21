import json


def sum_json(tree):
    child_sum = 0
    for child in tree:
        if isinstance(tree, dict):
            child = tree[child]

        if child == "red" and isinstance(tree, dict):
            return 0

        if isinstance(child, dict):
            child_sum += sum_json(child)
        elif isinstance(child, list):
            child_sum += sum_json(child)
        elif isinstance(child, int):
            child_sum += child
        else:
            pass
    return child_sum


with open("input_12.txt") as file:
    content = file.read()
    json_tree = json.loads(content)
    tree_sum = sum_json(json_tree)
    print(tree_sum)

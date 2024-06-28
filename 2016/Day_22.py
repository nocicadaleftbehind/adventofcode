import heapq
import re

EMPTY = 0
NORMAL = 1
WALL = 2

nodes = {}
node_info = {}
with open("input_22.txt") as file:
    for line in file:
        line = line[:-1]
        m = re.match("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%", line)
        if m:
            pos_x = int(m.group(1))
            pos_y = int(m.group(2))
            size = int(m.group(3))
            used = int(m.group(4))

            celltype = NORMAL
            if used >= 100:
                celltype = WALL
            elif used == 0:
                celltype = EMPTY
            nodes[(pos_x, pos_y)] = celltype
            node_info[(pos_x, pos_y)] = (size, used)

empty_node = [(x, y) for (x, y) in nodes.keys() if nodes[(x, y)] == EMPTY][0]
max_x = max([x for x, y in nodes.keys()])
max_y = max([y for x, y in nodes.keys()])


def viable_node_pairs(node_info):
    empty_node_size = node_info[empty_node][0]

    viable_nodes = 0
    for node in node_info.values():
        if 0 < node[1] <= empty_node_size:
            viable_nodes += 1
    return viable_nodes


def calc_moves(nodes, empty_node_pos, end_node_pos):
    new_states = []
    old_x = empty_node_pos[0]
    old_y = empty_node_pos[1]

    for new_pos_x, new_pos_y in [(old_x - 1, old_y), (old_x + 1, old_y), (old_x, old_y - 1), (old_x, old_y + 1)]:
        if new_pos_x < 0 or new_pos_x > max_x:
            continue
        if new_pos_y < 0 or new_pos_y > max_y:
            continue
        if nodes[(new_pos_x, new_pos_y)] == WALL:
            continue
        new_end_pos = end_node_pos
        if end_node_pos == (new_pos_x, new_pos_y):
            new_end_pos = (old_x, old_y)
        new_states.append(((new_pos_x, new_pos_y), new_end_pos))
    return new_states

def shorted_path(nodes):
    nodes_queue = [(0, 0, empty_node, (max_x, 0))]
    visited = set()
    while len(nodes_queue) > 0:
        _, length, empty_node_pos, end_node_pos = heapq.heappop(nodes_queue)
        if (empty_node_pos, end_node_pos) in visited:
            continue
        visited.add((empty_node_pos, end_node_pos))
        next_moves = calc_moves(nodes, empty_node_pos, end_node_pos)
        for next_empty, next_end in next_moves:
            if (next_empty, next_end) in visited:
                continue
            heuristic = length + next_end[0] + next_end[1]
            heapq.heappush(nodes_queue, (heuristic, length + 1, next_empty, next_end))
            if next_end[0] == 0 and next_end[1] == 0:
                return length + 1

print("PART 1")
print(viable_node_pairs(node_info))

print("PART 2")
print(shorted_path(nodes))

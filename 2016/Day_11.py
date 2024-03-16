import copy
import heapq
import itertools
import re

mappings = {
    "cobalt microchip": "CoM",
    "cobalt generator": "CoG",
    "curium microchip": "CuM",
    "curium generator": "CuG",
    "hydrogen microchip": "HM",
    "hydrogen generator": "HG",
    "lithium microchip": "LM",
    "lithium generator": "LG",
    "plutonium microchip": "PlM",
    "plutonium generator": "PlG",
    "promethium microchip": "PrM",
    "promethium generator": "PrG",
    "ruthenium microchip": "RM",
    "ruthenium generator": "RG",
}

max_floor = 0
floors = {"E": 0, }
with open("input_11.txt") as f:
    for i, line in enumerate(f):
        line = line.replace("-compatible", "")
        m = re.findall(r"a ([^ ]+ (generator|microchip))", line)
        for element in m:
            floors[mappings[element[0]]] = i
        max_floor = i


def floor_hash(state):
    s = ""
    s += str(state["E"]) + ","
    for floor in range(max_floor):
        for type in ["M", "G"]:
            num = len([1 for e, f in state.items() if f == floor and e.endswith(type)])
            s += str(num) + ","
    return s

def end_state(state):
    for floor in state.values():
        if floor != max_floor:
            return False
    return True


def heuristic(state):
    value = 0
    for floor in state.values():   
        value += (max_floor - floor) / 2 
    return value


def elements_on_same_floors(state, search_element):
    return [element for element, floor in state.items() if floor == state[search_element] and element != search_element]


def next_states(state):
    elevator_floor = state["E"]
    elevator_floor_elements = elements_on_same_floors(state, "E")

    valid_next_states = []
    for elements in itertools.chain(itertools.combinations(elevator_floor_elements, 2),
                                    itertools.combinations(elevator_floor_elements, 1)):
        for next_floor in [elevator_floor - 1, elevator_floor + 1]:
            next_state = copy.copy(state)
            if 0 > next_floor or next_floor > max_floor:
                continue
            
            if next_floor == elevator_floor - 1 and len([1 for v in state.values() if v <= next_floor]) == 0:
                continue

            next_state["E"] = next_floor
            for element in elements:
                next_state[element] = next_floor

            valid_state = True
            for element in next_state:
                if not element.endswith("M"):
                    continue
                generator = element[:-1] + "G"
                if generator in elements_on_same_floors(next_state, element):
                    continue

                all_generators = [element for element in next_state.keys() if
                                  element.endswith("G") and element != generator]
                if len(set(all_generators).intersection(elements_on_same_floors(next_state, element))) > 0:
                    valid_state = False

            if valid_state:
                valid_next_states.append(next_state)

    return valid_next_states

def search(floors):
    visited = set()
    queue = [(0, 0, floor_hash(floors), floors)]
    while len(queue) > 0:
        _, length, hash, floors = heapq.heappop(queue)
        if end_state(floors):
            return length
        
        for next_state in next_states(floors):
            hash = floor_hash(next_state)
            if hash in visited:
                continue
            visited.add(hash)
            
            heapq.heappush(queue, (length + heuristic(next_state) + 1, length + 1, hash, next_state))
    
    print("END WITHOUT SOLUTION")
    return -1

print("PART 1")
print(search(floors))

floors["EM"] = 0
floors["EG"] = 0
floors["DM"] = 0
floors["DG"] = 0
print("PART 2")
print(search(floors))

# works but needs speed up
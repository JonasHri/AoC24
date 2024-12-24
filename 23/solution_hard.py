# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()
    data = [x.strip().split("-") for x in data]

connections = set()
for a, b in data:
    connections.add((a, b))
    connections.add((b, a))

connections
# %%

from tqdm import tqdm

possible_choices = dict()

for a, b in connections:
    if a.startswith("t"):
        if a in possible_choices.keys():
            possible_choices[a].append(b)
        else:
            possible_choices[a] = [b]

possible_choices


true_connections = set()


def find_biggest(start, others, current):
    global current_max, biggest_connections, impossible_dense
    newest = current[-1]

    if current_max == len(others):
        return

    if current in impossible_dense:
        return

    for other in current[:-1]:
        if (newest, other) not in connections:
            impossible_dense.add(current)
            return

    if len(current) > current_max:
        print(len(current), current)
        current_max = len(current)
        biggest_connections.append(current)

    for other in others:
        if others not in current:
            find_biggest(start, others, current + (other,))

    return


biggest_each = dict()

current_max = 2
biggest_connections = []
impossible_dense = set()


for start, others in tqdm(possible_choices.items()):
    current_max = 2
    biggest_connections = []
    impossible_dense = set()
    find_biggest(start, others, (start,))

    biggest_each[start] = sorted(max(biggest_connections, key=lambda x: len(x)))


# %%
res = []
for start, others in tqdm(biggest_each.items()):
    full = True
    for first in range(len(others)):
        for second in range(first + 1, len(others)):
            a = others[first]
            b = others[second]
            if (a, b) not in connections:
                print(a, b)
                full = False
                break
        if not full:
            break

    if full:
        res.append(sorted(others + [start]))

res

pws = [",".join(x) for x in res]

pws

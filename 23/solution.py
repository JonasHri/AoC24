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
possible_choices = dict()

for a, b in connections:
    if a.startswith("t"):
        if a in possible_choices.keys():
            possible_choices[a].append(b)
        else:
            possible_choices[a] = [b]

possible_choices


true_connections = set()

for start, others in possible_choices.items():
    for first in range(len(others)):
        for second in range(first, len(others)):
            a = others[first]
            b = others[second]
            if (a, b) in connections:
                true_connections.add(tuple(sorted([start, a, b])))


len(true_connections), true_connections

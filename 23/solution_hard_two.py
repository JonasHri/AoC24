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
import random

nodes = set()

for a, _ in connections:
    nodes.add(a)


nodes = list(nodes)

nodes

max_full = []

for _ in range(1000):
    random.shuffle(nodes)
    full = []
    for n in nodes:
        dense = True
        for other in full:
            if (n, other) not in connections:
                dense = False
                break
        if dense:
            full.append(n)

    if len(full) > len(max_full):
        max_full = full

",".join(sorted(max_full))

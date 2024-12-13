# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

machines = []

for i in range(0, len(data), 4):
    a_button = data[i].split("+")
    ax, ay = a_button[-2].split(",")[0], a_button[-1]

    b_button = data[i + 1].split("+")
    bx, by = b_button[-2].split(",")[0], b_button[-1]

    prize = data[i + 2].split("=")
    px, py = prize[-2].split(",")[0], prize[-1]

    machine = {
        "a": np.array([ax, ay], dtype=int),
        "b": np.array([bx, by], dtype=int),
        "prize": np.array([px, py], dtype=int),
    }
    machines.append(machine)
# %%

total = 0
for machine in machines:
    solutions = []
    for a in range(100):
        for b in range(100):
            if (machine["a"] * a + machine["b"] * b == machine["prize"]).all():
                solutions.append(a * 3 + b)

    if len(solutions) > 0:
        total += min(solutions)

total

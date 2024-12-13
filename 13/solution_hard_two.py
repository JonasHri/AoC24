# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

machines = []

add = 0
add = 10000000000000

for i in range(0, len(data), 4):
    a_button = data[i].split("+")
    ax, ay = int(a_button[-2].split(",")[0]), int(a_button[-1])

    b_button = data[i + 1].split("+")
    bx, by = int(b_button[-2].split(",")[0]), int(b_button[-1])

    prize = data[i + 2].split("=")
    px, py = int(prize[-2].split(",")[0]) + add, int(prize[-1]) + add

    machine = {
        "a": [ax, ay],
        "b": [bx, by],
        "prize": [px, py],
    }
    machines.append(machine)
# %%
from tqdm import tqdm


total = 0
for machine in tqdm(machines):
    solutions = []

    for a in range(1000000):
        rem_x = machine["prize"][0] - a * machine["a"][0]
        if rem_x % machine["b"][0] != 0:
            continue
        b = rem_x // machine["b"][0]

        if machine["a"][1] * a + machine["b"][1] * b == machine["prize"][1]:
            solutions.append(3 * a + b)

    if len(solutions) > 0:
        total += min(solutions)

total

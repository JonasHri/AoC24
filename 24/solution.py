# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

wire_gate_split = data.index("\n")

wires_raw = [x.strip() for x in data[:wire_gate_split]]
gates_raw = [x.strip() for x in data[wire_gate_split + 1 :]]

wires = set()

for line in wires_raw:
    wires.add(line.split(":")[0])

for line in gates_raw:
    words = line.split(" ")
    wires.add(words[0])
    wires.add(words[2])
    wires.add(words[4])

wire_power = {wire: None for wire in wires}

for line in wires_raw:
    w, p = line.split(":")
    wire_power[w] = int(p)

wire_power

gate_funks = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}

# type in1 in2 out

gates = []

for line in gates_raw:
    in1, ty, in2, _, out = line.split(" ")

    gates.append((ty, in1, in2, out))


changes = True
while changes:
    changes = False
    for gate in gates:
        ty, in1, in2, out = gate

        if wire_power[in1] is not None and wire_power[in2] is not None and wire_power[out] is None:
            changes = True
            wire_power[out] = gate_funks[ty](wire_power[in1], wire_power[in2])

# %%
res = []
for x, y in wire_power.items():

    if x.startswith("z"):
        res.append((x, y))

res = sorted(
    res,
    key=lambda x: x[0],
)

print(int("".join(str(x[1]) for x in res[::-1]), 2))

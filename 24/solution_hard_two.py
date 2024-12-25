# %%
from random import randint
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

    gates.append([ty, in1, in2, out])

gates_og = deepcopy(gates)

# %%
gates = deepcopy(gates_og)

switching = [
    ["z12", "qdg"],
    ["z19", "vvf"],
    ["fgn", "dck"],
    ["nvh", "z37"],
]

switch_dict = dict()
for x, y in switching:
    switch_dict[x] = y
    switch_dict[y] = x


for gate in gates:
    ty, in1, in2, out = gate
    if out in switch_dict.keys():
        gate[-1] = switch_dict[out]


incorrect = set()
for _ in range(100):
    bit_length = 5
    bit_length = 45

    x_in = randint(0, 2**bit_length)
    y_in = randint(0, 2**bit_length)
    z_out = x_in + y_in

    for x in wire_power.keys():
        wire_power[x] = None

    for i, power in enumerate(f"{x_in:0{bit_length}b}"[::-1]):
        wire_power[f"x{i:02d}"] = int(power)

    for i, power in enumerate(f"{y_in:0{bit_length}b}"[::-1]):
        wire_power[f"y{i:02d}"] = int(power)

    expected = dict()

    for i, power in enumerate(f"{z_out:0{bit_length + 1}b}"[::-1]):
        expected[f"z{i:02d}"] = int(power)

    # print(x_in, y_in, z_out, expected)

    changes = True
    while changes:
        changes = False
        for gate in gates:
            ty, in1, in2, out = gate

            if wire_power[in1] is not None and wire_power[in2] is not None and wire_power[out] is None:
                changes = True
                wire_power[out] = gate_funks[ty](wire_power[in1], wire_power[in2])

    res = dict()
    for x, y in wire_power.items():

        if x.startswith("z"):
            res[x] = y

    for k in res.keys():
        if res[k] != expected[k]:
            incorrect.add(k)
print(sorted(list(incorrect)))
# %%

solutions = []

for a, b in switching:
    solutions.append(a)
    solutions.append(b)


",".join(sorted(solutions))

# %%
with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

machines = []

add = 10000000000000
add = 0

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

machines
# %%
import numpy as np

total = 0

for m in machines:

    mat = np.array(
        [
            [m["a"][0], m["b"][0]],
            [m["a"][1], m["b"][1]],
        ]
    )

    prize = np.array([[m["prize"][0]], [m["prize"][1]]])

    res = (prize.T @ np.linalg.inv(mat).T).flatten()

    if res[0] == int(res[0]) and res[1] == int(res[1]):
        print(res[0], res[1])
        total += int(res[0]) * 3 + int(res[1])

total

# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

warehouse = []

moves = ""

for line in data:
    print(line)
    if "#" in line:
        warehouse.append(list(line.strip()))

    if any([x in line for x in "^v<>"]):
        moves += line.strip()


warehouse = np.array(warehouse)
warehouse, moves

# %%

x, y = [a[0] for a in np.where(warehouse == "@")]

print(x, y)

for instruction in moves:
    if instruction == "^":
        view = list(warehouse[: x + 1, y][::-1])
        view_to_box = view[: view.index("#") + 1]
        view_rest = view[view.index("#") + 1 :]

        if "." not in view_to_box:
            continue

        view_to_box.remove(".")
        view_to_box = ["."] + view_to_box

        warehouse[: x + 1, y] = (view_to_box + view_rest)[::-1]
        x -= 1

    elif instruction == "v":
        view = list(warehouse[x:, y])
        view_to_box = view[: view.index("#") + 1]
        view_rest = view[view.index("#") + 1 :]

        if "." not in view_to_box:
            continue

        view_to_box.remove(".")
        view_to_box = ["."] + view_to_box

        warehouse[x:, y] = view_to_box + view_rest
        x += 1

    elif instruction == "<":
        view = list(warehouse[x, : y + 1])[::-1]
        view_to_box = view[: view.index("#") + 1]
        view_rest = view[view.index("#") + 1 :]

        if "." not in view_to_box:
            continue

        view_to_box.remove(".")
        view_to_box = ["."] + view_to_box

        warehouse[x, : y + 1] = (view_to_box + view_rest)[::-1]
        y -= 1

    elif instruction == ">":
        view = list(warehouse[x, y:])
        view_to_box = view[: view.index("#") + 1]
        view_rest = view[view.index("#") + 1 :]

        if "." not in view_to_box:
            continue

        view_to_box.remove(".")
        view_to_box = ["."] + view_to_box

        warehouse[x, y:] = view_to_box + view_rest
        y += 1


# %%

total = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i, j] == "O":
            total += i * 100 + j

total

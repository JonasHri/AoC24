# %%
import numpy as np
from copy import deepcopy


def pr(warehouse):
    for line in warehouse:
        print("".join(line))
    print()


with open("input.txt", "r") as f:
    data = f.readlines()

warehouse = []

moves = ""

scaler = {"#": "##", "O": "[]", ".": "..", "@": "@."}

for line in data:
    if "#" in line:
        extended_line = "".join([scaler[x] for x in list(line.strip())])
        warehouse.append(list(extended_line))

    if any([x in line for x in "^v<>"]):
        moves += line.strip()


fresh_warehouse = np.array(warehouse)
pr(warehouse), moves

# %%

warehouse = deepcopy(fresh_warehouse)

x, y = [a[0] for a in np.where(warehouse == "@")]


def check_above(x, y):
    global warehouse, checked

    if warehouse[x, y] == ".":
        return 0
    if warehouse[x, y] == "#":
        return 1
    if checked[x, y]:
        return 0

    checked[x, y] = 1
    if warehouse[x, y] == "[":
        other_y = y + 1
    else:
        other_y = y - 1

    return check_above(x - 1, y) + check_above(x, other_y)


for instruction in moves:
    if instruction == "^":
        above = warehouse[x - 1, y]
        if above == ".":
            warehouse[x - 1, y] = "@"
            warehouse[x, y] = "."
            x -= 1

        elif above == "#":
            continue
        else:
            checked = np.zeros_like(warehouse, dtype=int)
            if (check_above(x - 1, y)) == 0:
                for i in range(len(warehouse)):
                    for j in range(len(warehouse[0])):
                        if checked[i, j]:
                            tmp = warehouse[i - 1, j]
                            warehouse[i - 1, j] = warehouse[i, j]
                            warehouse[i, j] = "."

                warehouse[x, y] = "."
                x -= 1
                warehouse[x, y] = "@"

        # view = list(warehouse[: x + 1, y][::-1])
        # view_to_box = view[: view.index("#") + 1]
        # view_rest = view[view.index("#") + 1 :]

        # if "." not in view_to_box:
        #     continue

        # view_to_box.remove(".")
        # view_to_box = ["."] + view_to_box

        # warehouse[: x + 1, y] = (view_to_box + view_rest)[::-1]

    elif instruction == "v":
        warehouse = warehouse[::-1]
        x, y = [a[0] for a in np.where(warehouse == "@")]

        above = warehouse[x - 1, y]
        if above == ".":
            warehouse[x - 1, y] = "@"
            warehouse[x, y] = "."
            x -= 1

        elif above == "#":
            pass
        else:
            checked = np.zeros_like(warehouse, dtype=int)
            if (check_above(x - 1, y)) == 0:
                for i in range(len(warehouse)):
                    for j in range(len(warehouse[0])):
                        if checked[i, j]:
                            tmp = warehouse[i - 1, j]
                            warehouse[i - 1, j] = warehouse[i, j]
                            warehouse[i, j] = "."

                warehouse[x, y] = "."
                x -= 1
                warehouse[x, y] = "@"

        warehouse = warehouse[::-1]
        x, y = [a[0] for a in np.where(warehouse == "@")]

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

    pr(warehouse)
# %%

total = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i, j] == "[":
            total += i * 100 + j

total

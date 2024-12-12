# %%
import numpy as np
from copy import deepcopy
from enum import Enum


with open("input.txt", "r") as f:
    data = f.readlines()
data = np.array([list(x.strip()) for x in data])
data

big_data = np.full((len(data) + 2, len(data[0]) + 2), ".")

big_data[1:-1, 1:-1] = data

data = deepcopy(big_data)
data
# %%

visited = np.zeros_like(data, dtype=int)
is_area = np.zeros_like(data, dtype=int)


def get_area(plant, i, j):
    global data
    global visited
    global is_area

    if data[i, j] == ".":
        return 0

    if data[i, j] != plant:
        return 0

    if visited[i, j] == 1:
        return 0

    visited[i, j] = 1
    is_area[i, j] = 1

    return (
        1
        + get_area(plant, i + 1, j)
        + get_area(plant, i - 1, j)
        + get_area(plant, i, j + 1)
        + get_area(plant, i, j - 1)
    )


def get_perimeter(plant, i, j):
    global data
    global visited

    if data[i, j] == ".":
        is_perim[i, j] = 1
        return 1

    if data[i, j] != plant:
        is_perim[i, j] = 1
        return 1

    if visited[i, j] == 2:
        return 0

    visited[i, j] = 2

    return (
        get_perimeter(plant, i + 1, j)
        + get_perimeter(plant, i - 1, j)
        + get_perimeter(plant, i, j + 1)
        + get_perimeter(plant, i, j - 1)
    )


total = 0
for i in range(1, len(data)):
    for j in range(1, len(data[0])):
        if visited[i, j] > 0:
            continue
        if data[i, j] == ".":
            continue

        is_area = np.zeros_like(data, dtype=int)
        is_perim = np.zeros_like(data, dtype=int)

        area = get_area(data[i, j], i, j)

        perimiter = 0

        # top
        on_line = False
        for a in range(1, len(data) - 1):
            for b in range(1, len(data[0]) - 1):
                if is_area[a, b] and not is_area[a + 1, b]:
                    if not on_line:
                        is_area[a, b] = 8
                        perimiter += 1
                    on_line = True
                else:
                    on_line = False

        # bot
        on_line = False
        for a in range(1, len(data) - 1):
            for b in range(1, len(data[0]) - 1):
                if is_area[a, b] and not is_area[a - 1, b]:
                    if not on_line:
                        is_area[a, b] = 8
                        perimiter += 1
                    on_line = True
                else:
                    on_line = False

        is_area = is_area.T
        # right
        on_line = False
        for a in range(1, len(data) - 1):
            for b in range(1, len(data[0]) - 1):
                if is_area[a, b] and not is_area[a + 1, b]:
                    if not on_line:
                        is_area[a, b] = 8
                        perimiter += 1
                    on_line = True
                else:
                    on_line = False

        # left
        on_line = False
        for a in range(1, len(data) - 1):
            for b in range(1, len(data[0]) - 1):
                if is_area[a, b] and not is_area[a - 1, b]:
                    if not on_line:
                        is_area[a, b] = 8
                        perimiter += 1
                    on_line = True
                else:
                    on_line = False

        print(data[i, j], area, perimiter)

        total += area * perimiter

total
# %%

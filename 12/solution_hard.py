# %%
import numpy as np
from copy import deepcopy
from enum import Enum


class d(Enum):
    up = 0
    right = 1
    down = 2
    left = 3


with open("input_easy.txt", "r") as f:
    data = f.readlines()
data = np.array([list(x.strip()) for x in data])
data

big_data = np.full((len(data) + 2, len(data[0]) + 2), ".")

big_data[1:-1, 1:-1] = data

data = deepcopy(big_data)
data
# %%

visited = np.zeros_like(data, dtype=int)
is_perim = np.zeros_like(data, dtype=int)


def get_area(plant, i, j):
    global data
    global visited

    if data[i, j] == ".":
        return 0

    if data[i, j] != plant:
        return 0

    if visited[i, j] == 1:
        return 0

    visited[i, j] = 1

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

        is_perim = np.zeros_like(data, dtype=int)

        area = get_area(data[i, j], i, j)
        perimiter = get_perimeter(data[i, j], i, j)
        if data[i, j] == "F":
            print(is_perim)

        on_line = False
        for a in range(len(data)):
            for b in range(len(data[0])):
                if on_line and is_perim[a, b] == 1:
                    perimiter -= 1

                on_line = is_perim[a, b] == 1

        on_line = False
        is_perim = is_perim.T
        for a in range(len(data)):
            for b in range(len(data[0])):
                if on_line and is_perim[a, b] == 1:
                    perimiter -= 1

                on_line = is_perim[a, b] == 1

        print(data[i, j], area, perimiter)

        total += area * perimiter

total
# %%

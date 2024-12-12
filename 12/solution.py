# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()
data = np.array([list(x.strip()) for x in data])
data
# %%

visited = np.zeros_like(data, dtype=int)


def get_area(plant, i, j):
    global data
    global visited

    if 0 > i or i >= len(data) or 0 > j or j >= len(data):
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

    if 0 > i or i >= len(data) or 0 > j or j >= len(data):
        return 1

    if data[i, j] != plant:
        return 1

    if visited[i, j] == 2:
        return 0

    visited[i, j] = 2

    return (
        0
        + get_perimeter(plant, i + 1, j)
        + get_perimeter(plant, i - 1, j)
        + get_perimeter(plant, i, j + 1)
        + get_perimeter(plant, i, j - 1)
    )

    pos = [
        [i + 0, j + 1],
        [i + 0, j - 1],
        [i + 1, j + 0],
        [i - 1, j + 0],
    ]
    fences = 0

    for a, b in pos:
        if 0 > a or a >= len(data) or 0 > b or b >= len(data):
            fences += 1
            continue

        if data[a, b] != plant:
            fences += 1

    return fences


total = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if visited[i, j] > 0:
            continue

        area = get_area(data[i, j], i, j)
        perimiter = get_perimeter(data[i, j], i, j)

        print(data[i, j], area, perimiter)

        total += area * perimiter


total

# %%
import numpy as np
from copy import deepcopy
from math import cos, sin, pi

with open("input.txt", "r") as f:
    data = f.readlines()

    data = [list(x.strip()) for x in data]

data = np.array(data)
# %%

print(data[139][1], data[1, 139])

ex, ey = [x[0] for x in np.where(data == "E")]

startx, starty = [x[0] for x in np.where(data == "S")]


x, y, rot, score = 0, 1, 2, 3
reindeer = [
    [startx, starty, 0, 0],
]

visited = {(startx, starty, 0): 0}


def progress(x, y, score):
    global ex, ey
    rem_dist = np.sqrt((x - ex) ** 2 + (y - ey) ** 2)
    return score + rem_dist


while True:
    closest = min(reindeer, key=lambda ren: progress(ren[x], ren[y], ren[score]))
    reindeer.remove(closest)
    if closest[x] == ex and closest[y] == ey:
        print(closest[score])
        break

    keys = []

    next_x = closest[x] + int(sin(closest[rot] * pi / 2))
    next_y = closest[y] + int(cos(closest[rot] * pi / 2))
    if data[next_x, next_y] != "#":
        keys.append(((next_x, next_y, closest[rot]), closest[score] + 1))

    keys.append(((closest[x], closest[y], (closest[rot] + 1) % 4), closest[score] + 1000))
    keys.append(((closest[x], closest[y], (closest[rot] + 3) % 4), closest[score] + 1000))

    for key, val in keys:
        if val < visited.get(key, 1e50):
            visited[key] = val
            reindeer.append([*key, val])

# %%
import numpy as np
from copy import deepcopy
from math import cos, sin, pi

with open("input.txt", "r") as f:
    data = f.readlines()

    data = [list(x.strip()) for x in data]

data = np.array(data)
# %%

res = deepcopy(data)


ex, ey = [x[0] for x in np.where(data == "E")]

startx, starty = [x[0] for x in np.where(data == "S")]


x, y, rot, score, path = 0, 1, 2, 3, 4
reindeer = [
    [startx, starty, 0, 0, set([(startx, starty)])],
]

visited = {(startx, starty, 0): 0}

shortest_path = 90440


def progress(x, y, score):
    global ex, ey
    rem_dist = np.sqrt((x - ex) ** 2 + (y - ey) ** 2)
    return score + rem_dist


while True:
    if len(reindeer) == 0:
        break
    closest = min(reindeer, key=lambda ren: progress(ren[x], ren[y], ren[score]))
    reindeer.remove(closest)
    if closest[score] > shortest_path:
        continue

    if closest[x] == ex and closest[y] == ey:
        shortest_path = min(shortest_path, closest[score])
        for xc, yc in closest[path]:
            res[xc, yc] = "O"
        print(closest[score])

    keys = []

    next_x = closest[x] + int(sin(closest[rot] * pi / 2))
    next_y = closest[y] + int(cos(closest[rot] * pi / 2))
    if data[next_x, next_y] != "#":
        new_path = deepcopy(closest[path])
        new_path.add((next_x, next_y))
        keys.append(((next_x, next_y, closest[rot]), closest[score] + 1, new_path))

    keys.append(((closest[x], closest[y], (closest[rot] + 1) % 4), closest[score] + 1000, closest[path]))
    keys.append(((closest[x], closest[y], (closest[rot] + 3) % 4), closest[score] + 1000, closest[path]))

    for key, val, cpath in keys:
        if val <= visited.get(key, 1e50):
            visited[key] = val
            reindeer.append([*key, val, cpath])

# %%

(res == "O").sum()

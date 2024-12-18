# %%
import numpy as np
from copy import deepcopy


def pr(maze):
    for line in maze:
        print("".join(line))
    print()


with open("input.txt", "r") as f:
    data = f.readlines()

maze = np.full((73, 73), ".")
maze[0] = "#"
maze[-1] = "#"
maze[:, 0] = "#"
maze[:, -1] = "#"
maze[1, 1] = "S"
maze[-2, -2] = "E"

for i in range(1024):

    a, b = [int(x) for x in data[i].strip().split(",")]
    maze[b + 1, a + 1] = "#"

pr(maze)
# %%


ex, ey = [x[0] for x in np.where(maze == "E")]

startx, starty = [x[0] for x in np.where(maze == "S")]

offsets = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

x, y, score = 0, 1, 2
reindeer = [
    [startx, starty, 0],
]

visited = {(startx, starty, 0): 0}


def progress(x, y, score):
    global ex, ey
    rem_dist = np.sqrt((x - ex) ** 2 + (y - ey) ** 2)
    return score + rem_dist


while True:
    print(len(reindeer))
    closest = min(reindeer, key=lambda ren: progress(ren[x], ren[y], ren[score]))
    reindeer.remove(closest)
    if closest[x] == ex and closest[y] == ey:
        print(closest[score])
        break

    keys = []

    for a, b in offsets:
        next_x = closest[x] + a
        next_y = closest[y] + b
        if maze[next_x, next_y] != "#":
            keys.append(((next_x, next_y), closest[score] + 1))

    for key, val in keys:
        if val < visited.get(key, 1e50):
            visited[key] = val
            reindeer.append([*key, val])

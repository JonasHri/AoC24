# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

maze = np.array([list(x.strip()) for x in data])
# %%


def get_time(maze):

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
        closest = min(reindeer, key=lambda ren: progress(ren[x], ren[y], ren[score]))
        reindeer.remove(closest)
        if closest[x] == ex and closest[y] == ey:
            res = closest[score]
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

    return res


get_time(maze)

# %%
from tqdm import tqdm

times = []

best = get_time(maze)

for i in tqdm(range(1, len(maze) - 1)):
    for j in range(1, len(maze[0]) - 1):

        if maze[i, j] == "#":

            new_maze = deepcopy(maze)
            new_maze[i, j] = "."

            new_time = get_time(new_maze)

            if new_time < best - 99:
                times.append(new_time)


len(times), times

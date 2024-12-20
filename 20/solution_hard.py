# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

maze = np.array([list(x.strip()) for x in data])
# %%


ex, ey = [x[0] for x in np.where(maze == "E")]

startx, starty = [x[0] for x in np.where(maze == "S")]

offsets = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

best_no_cheat = 9336
all_cheats = set()
times = []

x, y, score, cheat_time, cheat_pos = 0, 1, 2, 3, 4
reindeer = [
    [startx, starty, 0, 20, set()],
]

visited = {(startx, starty, 0): 0}


def progress(x, y, score):
    global ex, ey
    rem_dist = np.sqrt((x - ex) ** 2 + (y - ey) ** 2)
    return score + rem_dist


# %%

slowest = 0


while len(reindeer) > 0:
    closest = min(reindeer, key=lambda ren: progress(ren[x], ren[y], ren[score]))
    reindeer.remove(closest)

    if closest[score] > slowest + 10:
        slowest = closest[score]
        print(slowest, len(reindeer))

    if closest[x] == ex and closest[y] == ey:
        cheat_set = tuple(closest[cheat_pos])
        if cheat_set not in all_cheats:
            all_cheats.add(cheat_set)
            times.append(closest[score])

    keys = []

    for a, b in offsets:
        next_x = closest[x] + a
        next_y = closest[y] + b
        if len(closest[cheat_pos]) == 1:
            if closest[cheat_time] >= 1:  # continue cheating
                keys.append(((next_x, next_y), closest[score] + 1, closest[cheat_time] - 1, closest[cheat_pos]))
                if maze[next_x, next_y] != "#":  # stop cheating
                    cheat_set = deepcopy(closest[cheat_pos])
                    cheat_set.add((next_x, next_y))
                    keys.append(((next_x, next_y), closest[score] + 1, closest[cheat_time] - 1, cheat_set))

        elif maze[next_x, next_y] != "#":  # dont cheat
            keys.append(((next_x, next_y), closest[score] + 1, closest[cheat_time], closest[cheat_pos]))

        elif len(closest[cheat_pos]) == 0:  # start cheating
            cheat_set = set()
            cheat_set.add((x, y))
            keys.append(((next_x, next_y), closest[score] + 1, closest[cheat_time] - 1, cheat_set))

    for key, val, ct, cp in keys:
        if val <= min(visited.get(key, 1e50), best_no_cheat - 99):
            visited[key] = val
            reindeer.append([*key, val, ct, cp])

len(times), times
# %%

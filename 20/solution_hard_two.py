# %%
import numpy as np
from copy import deepcopy
from collections import deque

with open("input.txt", "r") as f:
    data = f.readlines()

maze = np.array([list(x.strip()) for x in data])
# %%


ex, ey = [int(x[0]) for x in np.where(maze == "E")]

startx, starty = [int(x[0]) for x in np.where(maze == "S")]

X, Y = maze.shape

offsets = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

best_no_cheat = 9336
seen = set()
res = set()
times = []

reindeer = deque([(startx, starty, 0, 20, None, None)])


DIST = {}
Q = deque([(0, ex, ey)])
while Q:
    d, x, y = Q.popleft()
    if (x, y) in DIST:
        continue
    DIST[(x, y)] = d
    for dx, dy in offsets:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < X and 0 <= new_y < Y and maze[new_x][new_y] != "#":
            Q.append((d + 1, new_x, new_y))


def find_cheat(d0, CHEAT_TIME):
    ans = set()
    Q = deque([(0, None, None, None, startx, starty)])
    SEEN = set()
    SAVE = 100
    while Q:
        score, cheat_start, cheat_end, cheat_time, x, y = Q.popleft()
        assert cheat_end is None
        if score >= d0 - SAVE:
            continue
        if maze[x][y] == "E":
            if cheat_end is None:
                cheat_end = (x, y)
            if score <= d0 - SAVE and (cheat_start, cheat_end) not in ans:
                # print(d,d0,r,c,cheat_start,cheat_end,cheat_time)
                ans.add((cheat_start, cheat_end))
        if (x, y, cheat_start, cheat_end, cheat_time) in SEEN:
            continue
        SEEN.add((x, y, cheat_start, cheat_end, cheat_time))
        # if len(SEEN) % 1000000 == 0:
        #    print(len(SEEN))

        if cheat_start is None:  # start cheat
            assert maze[x][y] != "#"
            Q.append((score, (x, y), None, CHEAT_TIME, x, y))
        if cheat_time is not None and maze[x][y] != "#":  # and cheat_time==0: # end cheat
            assert maze[x][y] in [".", "S", "E"]
            if DIST[(x, y)] <= d0 - 100 - score:
                ans.add((cheat_start, (x, y)))
                # if len(ans) % 1000 == 0:
                #    print(len(ans), d+DIST[(r,c)])
            # Q.append((d,cheat_start,(r,c),None,r,c))
        if cheat_time == 0:
            continue
        else:
            for dx, dy in offsets:
                new_x, new_y = x + dx, y + dy
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0 <= new_x < X and 0 <= new_y < Y:
                        Q.append((score + 1, cheat_start, None, cheat_time - 1, new_x, new_y))
                else:
                    if 0 <= new_x < X and 0 <= new_y < Y and maze[new_x][new_y] != "#":
                        Q.append((score + 1, cheat_start, cheat_end, cheat_time, new_x, new_y))
    # print(len(SEEN))
    return len(ans)


d0 = DIST[(startx, starty)]
print(find_cheat(d0, 2))
# print(find_cheat(d0, 20))

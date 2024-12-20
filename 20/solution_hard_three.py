# %%
import numpy as np
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

reindeer = deque([(startx, starty, 0, 20, None, None)])

DIST = np.full_like(maze, 1_000_000, dtype=int)
Q = deque([(0, ex, ey)])
while Q:
    d, x, y = Q.popleft()
    if DIST[x, y] < 1_000_000:
        continue
    DIST[x, y] = d
    for dx, dy in offsets:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < X and 0 <= new_y < Y and maze[new_x][new_y] != "#":
            Q.append((d + 1, new_x, new_y))

DIST

# %%

X_tab = np.zeros_like(maze, dtype=int)
for i in range(len(X_tab)):
    X_tab[:, i] = i


Y_tab = np.zeros_like(maze, dtype=int)
for i in range(len(Y_tab)):
    Y_tab[i, :] = i


def manh_dist(x, y):
    return np.abs(X_tab - y) + np.abs(Y_tab - x)


res = manh_dist(0, 0)

max_dist = 20
X_pat, Y_pat = np.where(DIST < 1_000_000)

total_possible = 0

for x, y in zip(X_pat, Y_pat):
    cheat_dist = manh_dist(x, y)
    cheat_rad = cheat_dist <= max_dist
    jumps = DIST + cheat_dist - DIST[x, y]
    possible_jumps = jumps[cheat_rad]
    total_possible += (possible_jumps <= -100).sum()

total_possible

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


def search(x, y):
    if x == ex and y == ey:
        return 1

    if visited[x, y]:
        return 0

    visited[x, y] = 1

    if maze[x, y] == "#":
        return 0

    return search(x + 1, y) + search(x - 1, y) + search(x, y + 1) + search(x, y - 1)


ex, ey = [x[0] for x in np.where(maze == "E")]

startx, starty = [x[0] for x in np.where(maze == "S")]


for i in range(1024, len(data)):

    a, b = [int(x) for x in data[i].strip().split(",")]
    maze[b + 1, a + 1] = "#"
    visited = np.zeros_like(maze, dtype=int)

    if not search(1, 1):
        print(a, b, i)
        break

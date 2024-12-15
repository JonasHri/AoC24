# %%
import numpy as np
from copy import deepcopy


robots = []
with open("input.txt", "r") as f:
    data = f.readlines()

    for line in data:
        line = line.replace("=", "=[", 2)
        line = line.replace(" ", "] ")
        line = line.replace("\n", "]")
        for expr in line.split():
            exec(expr)

        robot = [p[0], p[1], v[0], v[1]]
        robots.append(robot)
        print(line)
        print(robot)

robots = np.array(robots)

width = 11
height = 7

height = 103
width = 101

px, py, vx, vy = 0, 1, 2, 3
# %%

for i in range(100):

    for robot in robots:
        robot[px] = (robot[px] + robot[vx]) % width
        robot[py] = (robot[py] + robot[vy]) % height


pos = np.zeros((height, width), dtype=int)

for robot in robots:
    pos[robot[py], robot[px]] += 1

print(pos)

pos[height // 2, :] = 0

pos[:, width // 2] = 0

count = 1
quad = np.sum(pos[height // 2 :, width // 2 :])
print(quad, end=" ")
count *= quad

quad = np.sum(pos[height // 2 :, : width // 2])
print(quad, end=" ")
count *= quad

quad = np.sum(pos[: height // 2, width // 2 :])
print(quad, end=" ")
count *= quad

quad = np.sum(pos[: height // 2, : width // 2])
print(quad, end=" ")
count *= quad

print()

print(count)

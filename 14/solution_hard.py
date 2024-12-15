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
from tqdm import tqdm

min_cluster_factor = 999999

with open("res.txt", "w") as f:
    for i in tqdm(range(100000)):

        for robot in robots:
            robot[px] = (robot[px] + robot[vx]) % width
            robot[py] = (robot[py] + robot[vy]) % height

        m_x = np.mean(robots[:, px])
        m_y = np.mean(robots[:, py])

        cluster_factor = np.sum(
            np.sqrt((robots[:, px] - m_x) ** 2 + (robots[:, py] - m_y) ** 2)
        )

        if cluster_factor <= min_cluster_factor:

            min_cluster_factor = cluster_factor
            pos = np.zeros((height, width), dtype=int)

            for robot in robots:
                pos[robot[py], robot[px]] += 1

            f.write("\n number: " + str(i) + "\n")
            for a in range(len(pos)):
                for j in range(len(pos[0])):
                    f.write("x" if pos[a, j] else " ")
                f.write("\n")
            f.write("\n")

# %%
tree = np.zeros((height, width), dtype=int)

tree[:, width // 2] = 1

for i in range(len(tree)):
    for j in range(len(tree[0])):
        print(tree[i, j], end="")
    print()

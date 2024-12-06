# %%
import numpy as np


def pr(data):
    for line in data:
        print("".join(line))


with open("input.txt", "r") as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]
data = np.array(data)

data_fresh = data.copy()

# pr(data)
x_pos, y_pos = 0, 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            x_pos = j
            y_pos = i

x_start, y_start = x_pos, y_pos

directions = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0],
]

d = 0
try:
    while True:
        data[y_pos, x_pos] = "X"
        x_new = x_pos + directions[d][0]
        y_new = y_pos + directions[d][1]
        if data[y_new][x_new] == "#":
            d = (d + 1) % 4
        else:
            x_pos = x_new
            y_pos = y_new
except:
    pass

pr(data)
print((data == "X").sum())

# %%

loops = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "X":
            data_alt = data_fresh.copy()
            path = set()
            d = 0
            x_pos = x_start
            y_pos = y_start
            while True:
                if (x_pos, y_pos, d) in path:
                    loops += 1
                    break
                path.add((x_pos, y_pos, d))
                data_alt[y_pos][x_pos] = d
                x_new = x_pos + directions[d][0]
                y_new = y_pos + directions[d][1]

                if 0 <= x_new < len(data) and 0 <= y_new < len(data):
                    if data_alt[y_new][x_new] == "#" or (y_new == i and x_new == j):
                        d = (d + 1) % 4
                    else:
                        x_pos = x_new
                        y_pos = y_new

                else:
                    break

loops

# %%
import numpy as np


def pr(data):
    for line in data:
        print("".join(line))


with open("input_test.txt", "r") as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]
data = np.array(data)
pr(data)
# %%
x_pos, y_pos = 0, 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            x_pos = j
            y_pos = i

directions = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0],
]

current = 0

while 0 <= x_pos <= len(data) and 0 <= y_pos <= len(data):
    data[y_pos, x_pos] = "X"
    x_new = x_pos + directions[current][0]
    y_new = y_pos + directions[current][1]

    if data[y_new][x_new] == "#":
        current = (current + 1) % 4
    else:
        x_pos = x_new
        y_pos = y_new

# %%
pr(data)

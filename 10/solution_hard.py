# %%
import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]

data = np.array(data, dtype=int)

data
# %%


def trail(height, i, j, data):
    global seen
    n = len(data)
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if height != data[i, j]:
        return 0
    if height == 9 and data[i, j] == 9:
        if True:
            seen.add((i, j))
            return 1
        else:
            return 0

    else:
        nh = height + 1
        return (
            trail(nh, i + 1, j, data)
            + trail(nh, i - 1, j, data)
            + trail(nh, i, j + 1, data)
            + trail(nh, i, j - 1, data)
        )


heads = 0

for i in range(len(data)):
    for j in range(len(data)):
        if data[i, j] <= 0:
            seen = set()
            data[i, j] = 0
            data[i, j] = -trail(0, i, j, data)
            heads -= data[i, j]
            print(-data[i, j])

heads

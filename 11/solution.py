# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

data_fresh = [int(x) for x in data[0].strip().split()]
data_fresh
# %%
data = deepcopy(data_fresh)

for i in range(25):
    new_stones = []

    for stone in data:
        if stone == 0:
            new_stones.append(1)
            continue

        s_stone = str(stone)
        l = len(s_stone)
        if l % 2 == 0:
            # print(s_stone[:l//2], s_stone[l//2:], s_stone)
            new_stones.append(int(s_stone[: l // 2]))
            new_stones.append(int(s_stone[l // 2 :]))

        else:
            new_stones.append(stone * 2024)

    data = new_stones

len(data)

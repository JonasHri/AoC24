# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

data_fresh = [int(x) for x in data[0].strip().split()]
data_fresh
# %%
from functools import cache
from time import perf_counter


@cache
def count(stone, steps):
    if steps == 0:
        return 1

    steps -= 1
    next_stone = rules(stone)
    if type(next_stone) == type([]):
        return count(next_stone[0], steps) + count(next_stone[1], steps)
    else:
        return count(next_stone, steps)


def rules(stone):

    if stone == 0:
        return 1

    s_stone = str(stone)
    l = len(s_stone)
    if l % 2 == 0:
        # print(s_stone[:l//2], s_stone[l//2:], s_stone)
        return [int(s_stone[: l // 2]), int(s_stone[l // 2 :])]

    else:
        return stone * 2024


start = perf_counter()
total = 0
steps = 75
for stone in data_fresh:
    total += count(stone, steps)

total, perf_counter() - start

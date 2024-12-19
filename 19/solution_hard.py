# %%
import numpy as np
from copy import deepcopy
from tqdm import tqdm
from time import perf_counter

from functools import cache

with open("input.txt", "r") as f:
    data = f.readlines()

towels = data[0].strip().split(", ")
towels = sorted(towels, key=lambda x: -len(x))
patterns = [x.strip() for x in data[2:]]
patterns


@cache
def fit(pattern: str):
    # print(current)
    if not pattern:
        return 1

    res = 0
    for towel in towels:

        if pattern.startswith(towel):
            res += fit(pattern[len(towel) :])

    return res


total = 0
for pattern in tqdm(patterns):
    total += fit(pattern)
total

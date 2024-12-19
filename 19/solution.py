# %%
import numpy as np
from copy import deepcopy
from tqdm import tqdm
from time import perf_counter

with open("input.txt", "r") as f:
    data = f.readlines()

towels = data[0].strip().split(", ")
towels = sorted(towels, key=lambda x: -len(x))
patterns = [x.strip() for x in data[2:]]
patterns


def fit(current: str, pattern: str):
    # print(current)
    if pattern == current:
        return 1

    if not pattern.startswith(current):
        return 0

    for towel in towels:
        next_current = current + towel
        if fit(next_current, pattern):
            return 1

    return 0


total = 0
for pattern in tqdm(patterns):
    if fit("", pattern):
        print("yes: ", pattern)
    else:
        print("no : ", pattern)

total

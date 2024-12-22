# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()


starts = [int(x.strip()) for x in data]
starts
# %%


def mix(secret, other):
    return secret ^ other


def prune(secret):
    return secret % 16777216


def calculate_next(secret):
    res = secret * 64
    secret = mix(secret, res)
    secret = prune(secret)

    res = secret // 32
    secret = mix(secret, res)

    secret = prune(secret)

    res = secret * 2048
    secret = mix(secret, res)

    return prune(secret)


start = 123
for _ in range(10):
    start = calculate_next(start)
    print(start)

# %%

# starts = [1,10,100,2024]
total = 0
for start in starts:
    secret = start
    for i in range(2000):
        secret = calculate_next(secret)

    total += secret
    print(start, secret)

total

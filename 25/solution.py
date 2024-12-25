# %%
import numpy as np
from copy import deepcopy

key_locks = [[]]
with open("input.txt", "r") as f:
    data = f.readlines()

for line in data:
    clean = line.strip()
    if clean == "":
        key_locks.append([])

    else:
        nums = [0 if x == "." else 1 for x in list(clean)]
        key_locks[-1].append(nums)

key_locks = np.array(key_locks)
key_locks

keys = []
locks = []


for kl in key_locks:
    if kl[0].sum() == 0:
        print(kl)
        keys.append(np.sum(kl, axis=0) - 1)
    else:
        locks.append(np.sum(kl, axis=0) - 1)


combs = 0
for key in keys:
    for lock in locks:
        if (key + lock <= 5).all():
            combs += 1

combs
# %%

locks

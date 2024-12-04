# %%
import numpy as np

left = []
right = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left = np.array(sorted(left))
right = np.array(sorted(right))

# %%
res = sum([np.sum(i * (i == right)) for i in left])
res

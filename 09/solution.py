# %%
with open("input.txt", "r") as f:
    data = f.readlines()[0].strip()

data
# %%
import numpy as np
import copy

is_data = True
id = 0
disk = []

for space in data:
    space = int(space)
    if is_data:
        disk = disk + [id] * space
        id += 1
    else:
        disk = disk + [-1] * space

    is_data = not is_data

og_disk = copy.deepcopy(disk)
# %%

disk = copy.deepcopy(og_disk)

for i in range(len(disk) - 1, 0, -1):
    first_free = disk.index(-1)
    if first_free < i:
        disk[first_free] = disk[i]
        disk[i] = -1
    else:
        break

disk
# %%
total = 0
for i in range(len(disk)):
    if disk[i] == -1:
        break

    total += i * disk[i]

total

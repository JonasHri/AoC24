# %%


def pr(disk):
    print("".join([str(x) if x != -1 else "." for x in disk]))


with open("input_e.txt", "r") as f:
    data = f.readlines()[0].strip()

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
pr(disk)
# %%

disk = copy.deepcopy(og_disk)

i = len(disk) - 1

while i > 0:
    if disk[i] == -1:
        i -= 1
        continue

    cur_size = 0
    cur_id = disk[i]
    while i > 0:
        if disk[i] == cur_id:
            cur_size += 1
            i -= 1
        else:
            break
    # print("found ", cur_id, cur_size, i, disk[i])
    j = 0
    while j <= i:
        if disk[j] != -1:
            j += 1
            continue

        empty_size = 0
        found_space = False
        while j <= i:
            if empty_size >= cur_size:
                found_space = True
                break
            if disk[j] == -1:
                j += 1
                empty_size += 1
            else:
                j += 1
                break

        if found_space:
            # print("empty: ", j, empty_size, disk[j])
            # print()

            for a in range(i + 1, i + cur_size + 1):
                disk[a] = -1

            for a in range(j - 1, j - cur_size - 1, -1):
                disk[a] = cur_id

            break

        # i -= 1

pr(disk)

# %%
total = 0
for i in range(len(disk)):
    if disk[i] == -1:
        continue

    total += (i) * disk[i]

# 6183633059094
# 6183879177045 with i+1
total

# %%
seen = set()
i = 0
cur_number = -3
while i < len(disk):
    if disk[i] == -1:
        if disk[i - 1] in seen:
            print("wrong")
            break
        while disk[i] == -1 and i < len(disk) - 1:
            i += 1

    cur_number = disk[i]
    while disk[i] == cur_number and i < len(disk) - 1:
        i += 1
    i += 1
# %%
import numpy as np

d_np = np.array(disk)
o_np = np.array(og_disk)

for id in set(disk):
    if np.sum(d_np == id) != np.sum(o_np == id):
        print(id)
        break

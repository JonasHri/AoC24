# %%
def pr(disk):
    result = []
    for file in disk:
        if file[0] == "empty":
            result = result + ["."] * file[1]
        else:
            result = result + [str(file[0])] * file[1]

    print("".join(result))

    total = 0
    for i, x in enumerate(result):
        if x != ".":
            total += i * int(x)

    return total


# %%
import copy

with open("input.txt", "r") as f:
    data = f.readlines()[0].strip()

data
# %%
is_data = True
id = 0
disk = []
for space in data:
    space = int(space)
    if is_data:
        disk = disk + [[id, space]]
        id += 1
    else:
        if space > 0:
            disk = disk + [["empty", space]]

    is_data = not is_data
disk


def defrag(disk):
    new_disk = [copy.deepcopy(disk[0])]
    for file in disk[1:]:
        if new_disk[-1][0] == file[0]:
            new_disk[-1][1] += file[1]
            new_disk.insert(-1, ["empty", 0])
        else:
            new_disk.append(file)

    return new_disk


i = len(disk)
while i >= 0:
    print(i)
    # i = min(len(disk), i)
    # pr(disk)
    i -= 1
    if disk[i][0] == "empty":
        continue
    for j in range(i):
        # print(j)
        if j >= i:
            break
        if disk[j][0] != "empty":
            continue

        if disk[j][1] == disk[i][1]:
            disk[j][0] = disk[i][0]
            disk[i][0] = "empty"
            disk = defrag(disk)
            break

        if disk[j][1] < disk[i][1]:
            continue

        disk[j][1] -= disk[i][1]
        disk.insert(j, copy.deepcopy(disk[i]))
        disk[i + 1][0] = "empty"
        disk = defrag(disk)
        i += 1
        break


pr(disk)

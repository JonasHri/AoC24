# %%
import numpy as np


def pr(data):
    for line in data:
        print("".join(line))


with open("input.txt", "r") as f:
    data = f.readlines()

data = np.array([list(x.strip()) for x in data])
pr(data)
# %%
antinodes = np.zeros_like(data, dtype=int)
antena_types = set()

culprit = False

for i in range(len(data)):
    for j in range(len(data[0])):
        antenna_type = data[i, j]

        if antenna_type == ".":
            continue

        for a in range(len(data)):
            for b in range(len(data)):
                other = data[a, b]
                if other != antenna_type:
                    continue
                if a == i and b == j:
                    continue

                diff_f = i - a  # from a to i
                diff_s = j - b  # from b to j

                left_x = i + diff_f
                left_y = j + diff_s

                right_x = a - diff_f
                right_y = b - diff_s

                try:
                    while 0 <= left_x < len(data) and 0 <= left_y <= len(data[0]):
                        antinodes[left_x, left_y] = 1
                        left_x += diff_f
                        left_y += diff_s
                except IndexError:
                    pass
                try:
                    while 0 <= right_x < len(data) and 0 <= right_y <= len(data[0]):
                        antinodes[right_x, right_y] = 1
                        right_x -= diff_f
                        right_y -= diff_s
                except IndexError:
                    pass


antinodes[data != "."] = 1


res = data.copy()
res[antinodes == 1] = "#"


pr(res)

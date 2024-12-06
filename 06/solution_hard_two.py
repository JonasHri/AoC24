# %%
import numpy as np
import copy
from tqdm import tqdm

with open("input.txt", "r") as f:
    data_fresh = f.readlines()

data_fresh = [list(x.strip()) for x in data_fresh]
data_fresh = np.array(data_fresh)
data_fresh
# %%

loops = 0

for a in tqdm(range(len(data_fresh))):
    for b in range(len(data_fresh)):
        data = copy.deepcopy(data_fresh)

        try:
            x_pos, y_pos = 0, 0

            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == "^":
                        x_pos = j
                        y_pos = i

            if x_pos == b and y_pos == a:
                print(a, b)
                1 / 0

            data[a][b] = "#"

            directions = [
                [0, -1],
                [1, 0],
                [0, 1],
                [-1, 0],
            ]

            current = 0

            for _ in range(25_000):
                data[y_pos, x_pos] = "X"
                x_new = x_pos + directions[current][0]
                y_new = y_pos + directions[current][1]

                if data[y_new][x_new] == "#":
                    current = (current + 1) % 4
                else:
                    x_pos = x_new
                    y_pos = y_new
            loops += 1
        except:
            pass

print(loops)

# %%
print((data == "X").sum())
for i in range(len(data)):
    for j in range(len(data)):
        print(data[i, j], end=" ")
    print()

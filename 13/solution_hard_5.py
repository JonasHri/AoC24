# %%
with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

machines = []

add = 0
add = 10000000000000

for i in range(0, len(data), 4):
    a_button = data[i].split("+")
    ax, ay = int(a_button[-2].split(",")[0]), int(a_button[-1])

    b_button = data[i + 1].split("+")
    bx, by = int(b_button[-2].split(",")[0]), int(b_button[-1])

    prize = data[i + 2].split("=")
    px, py = int(prize[-2].split(",")[0]) + add, int(prize[-1]) + add

    machine = {
        "a": [ax, ay],
        "b": [bx, by],
        "prize": [px, py],
    }
    machines.append(machine)

machines
# %%
import numpy as np

total = 0

x, y = 0, 1

for m in machines:

    m_a = (m["prize"][x] * m["b"][y] - m["prize"][y] * m["b"][x]) / (m["b"][y] * m["a"][x] - m["b"][x] * m["a"][y])
    m_b = (m["prize"][x] * m["a"][y] - m["prize"][y] * m["a"][x]) / (m["b"][x] * m["a"][y] - m["b"][y] * m["a"][x])
    if m_a == int(m_a) and m_b == int(m_b):
        total += 3 * m_a + m_b


total

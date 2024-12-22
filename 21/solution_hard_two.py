# %%
import numpy as np
from copy import deepcopy
import itertools

with open("input.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

data
# %%

keypad1 = np.array(
    [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3],
        ["n", 0, "A"],
    ]
)

keypad2 = np.array(
    [
        ["n", "^", "A"],
        ["<", "v", ">"],
    ]
)


def get_moves(start, end, keypad):
    sx, sy = [x[0] for x in np.where(keypad == str(start))]
    tx, ty = [x[0] for x in np.where(keypad == str(end))]

    dx = tx - sx
    dy = ty - sy

    lr = ">" if dy > 0 else "<"
    ud = "^" if dx < 0 else "v"

    moves = []

    if keypad[sx, sy + dy] != "n" and dy != 0:
        moves.append(lr * abs(dy) + ud * abs(dx) + "A")

    if keypad[sx + dx, sy] != "n" and dx != 0:
        moves.append(ud * abs(dx) + lr * abs(dy) + "A")

    if dx == dy == 0:
        moves.append("A")

    score = {key: i for i, key in enumerate(">^v<")}

    if len(moves) == 2:
        return [min(moves, key=lambda x: score[x[-2]])]
    else:
        return moves


get_moves("A", 2, keypad1)

# %%
from tqdm import tqdm
from collections import Counter

total = 0
robot_num = 25

test_data = ["029A", "980A", "179A", "456A", "379A"]

for code in data:
    first_moves = []
    third_seq = ""
    for start, stop in zip("A" + code, code):
        first_moves.append(get_moves(start, stop, keypad1))

    current_seqs = [dict(Counter(x)) for x in itertools.product(*first_moves)]
    for i in range(robot_num):
        all_seq = []
        for seq in current_seqs:
            next_seqs = dict()
            for key, val in seq.items():
                moves = []
                for start, stop in zip("A" + key, key):

                    moves.append(get_moves(start, stop, keypad2)[0])

                for move in moves:
                    next_seqs[move] = next_seqs.get(move, 0) + val

            all_seq.append(next_seqs)

        current_seqs = all_seq

    shortest_len = min(sum(len(key) * val for key, val in x.items()) for x in current_seqs)
    # print(shortest_len)

    total += int(code[:-1]) * shortest_len
    # print(code, min(len(x) for x in next_seqs), int(code[:-1]))


print(total)

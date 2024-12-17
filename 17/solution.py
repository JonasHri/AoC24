# %%
import numpy as np
from copy import deepcopy

with open("input_easy.txt", "r") as f:
    data = f.readlines()

A = int(data[0].strip().split(":")[1])
B = int(data[1].strip().split(":")[1])
C = int(data[2].strip().split(":")[1])


def combo(bit):
    global A, B, C
    res = [0, 1, 2, 3, A, B, C, 999999]
    return res[bit]


instructions = [int(x) for x in data[4].split(":")[1].split(",")]
pointer = 0
out_str = []


def adv(other):
    global A
    A = A // (2 ** combo(other))


def bxl(other):
    global B
    B = B ^ other


def bst(other):
    global B
    B = combo(other) % 8


def jnz(other):
    global A, pointer
    if A == 0:
        pointer += 1
    else:
        pointer = other - 2


def bxc(other):
    global B, C
    B = B ^ C


def out(other):
    global out_str
    out_str.append(str(combo(other) % 8))


def bdv(other):
    global A, B
    B = A // (2 ** combo(other))


def cdv(other):
    global A, C
    C = A // (2 ** combo(other))


ops = [
    adv,
    bxl,
    bst,
    jnz,
    bxc,
    out,
    bdv,
    cdv,
]

# C = 9
# instructions = [2, 6]

# A = 10
# instructions = [5, 0, 5, 1, 5, 4]

# A = 2024
# instructions = [0, 1, 5, 4, 3, 0]

# B = 29
# instructions = [1, 7]

# B = 2024
# C = 43690
# instructions = [4, 0]


# %%

A = 16899008

while 0 <= pointer < len(instructions) - 1:
    print(pointer, ops[instructions[pointer]].__name__, instructions[pointer + 1])
    ops[instructions[pointer]](instructions[pointer + 1])
    pointer += 2

print(f"{A=}, {B=}, {C=}")
print(",".join(out_str))

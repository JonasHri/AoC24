# %%
import numpy as np
from copy import deepcopy

with open("input_help.txt", "r") as f:
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
    out_str.append(combo(other) % 8)


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


# %%

correct_part = []
for pos in range(len(instructions)):
    corret_at_pos = []

    for i in range(0, 2 ** (7 + 3)):
        A = i * ((2**3) ** pos)
        a_start = A
        B = 0
        C = 0
        pointer = 0
        out_str = []

        while 0 <= pointer < len(instructions) - 1:
            # print(pointer, ops[instructions[pointer]].__name__, instructions[pointer + 1])
            ops[instructions[pointer]](instructions[pointer + 1])
            pointer += 2

        if len(out_str) > pos:
            if out_str[pos] == instructions[pos]:
                corret_at_pos.append(a_start)

    correct_part.append(corret_at_pos)


print(f"{A=}, {B=}, {C=}")
print(",".join(str(x) for x in out_str))


# %%

cp_bin = [["{:0b}".format(binary) for binary in position] for position in correct_part]


forward_check = 2**7
possible_solutions = []


def find_correct(index, current_num):

    if index == len(correct_part):
        possible_solutions.append(current_num)
        return current_num

    current_relevant = current_num // ((2**3) ** index)

    next_number_candiates = correct_part[index]
    for next_number in next_number_candiates:

        next_relevant = next_number // ((2**3) ** index)

        if current_relevant % forward_check == next_relevant % forward_check:
            find_correct(index + 1, next_number | current_num)


for num in correct_part[0]:
    find_correct(1, num)

possible_solutions
# %%

num = min(possible_solutions)
print(num)
print(instructions)

A = num
A = 16247842866690
a_start = A
B = 0
C = 0
pointer = 0
out_str = []

while 0 <= pointer < len(instructions) - 1:
    # print(pointer, ops[instructions[pointer]].__name__, instructions[pointer + 1])
    ops[instructions[pointer]](instructions[pointer + 1])
    pointer += 2

print(out_str)

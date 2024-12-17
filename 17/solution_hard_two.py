# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()

A = int(data[0].strip().split(":")[1])
B = int(data[1].strip().split(":")[1])
C = int(data[2].strip().split(":")[1])
printing = True


def combo(bit, adr=False):
    global A, B, C, printing
    res = [0, 1, 2, 3, A, B, C, 999999]
    if adr:
        res = ["0", "1", "2", "3", "A", "B", "C", "99999999999"]
    return res[bit]


instructions = [int(x) for x in data[4].split(":")[1].split(",")]
pointer = 0
out_str = []
cont_cur = True


def adv(other):
    global A
    A = A // (2 ** combo(other))
    if printing:
        print(f"A = A // 2**{combo(other, adr=True)}")


def bxl(other):
    global B
    B = B ^ other
    if printing:
        print(f"B = B ^ {other}")


def bst(other):
    global B
    B = combo(other) % 8
    if printing:
        print(f"B = {combo(other, adr=True)} % 8")


def jnz(other):
    global A, pointer
    if A == 0:
        pointer += 1
    else:
        pointer = other - 2

    if printing:
        if A == 0:
            print("go next")
        else:
            print("go", other)


def bxc(other):
    global B, C
    B = B ^ C
    if printing:
        print("B = B ^ C")


def out(other):
    global out_str
    global cont_cur
    global instructions
    out_str.append(str(combo(other) % 8))
    if printing:
        print(f"printing {combo(other, adr=True)} % 8")
    # out_loc = [0, 1, 2, 3, "A", "B", "C", 999999][other % 8]
    # print(out_loc)
    # if instructions[len(out_str) - 1] != combo(other) % 8:
    #     # print(out_str, instructions)
    #     cont_cur = False


def bdv(other):
    global A, B
    B = A // (2 ** combo(other))
    if printing:
        print(f"B = A // 2**{combo(other, adr=True)}")


def cdv(other):
    global A, C
    C = A // (2 ** combo(other))
    if printing:
        print(f"C = A // 2**{combo(other, adr=True)}")


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


lowest = 0
found = False
while not found:
    # A = lowest
    # A = lowest
    B = 0
    C = 0
    out_str = []
    pointer = 0
    cont_cur = True

    while 0 <= pointer < len(instructions) - 1 and cont_cur:
        # print(pointer, ops[instructions[pointer]].__name__, instructions[pointer + 1])
        ops[instructions[pointer]](instructions[pointer + 1])
        pointer += 2

    outint = [int(x) for x in out_str]

    if outint == instructions:
        print(lowest)
        break

    lowest += 1
    break

print(f"{A=}, {B=}, {C=}")
print(",".join(out_str))

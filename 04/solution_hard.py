# %%
print(f"{ord('A')=} {ord('M')=} {ord('S')=}")
import scipy
import numpy as np
import scipy.signal

with open("input_hard.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
data = [list(line) for line in data]
data = np.array(data)

v_ord = np.vectorize(ord)

data_int = v_ord(data)
data_int
# %%
wanted = ord("A") * 1_000_000 + (ord("M") + ord("S")) * 1_000 + ord("M") + ord("S")
conv = np.array(
    [
        [1_000, 0, 1],
        [0, 1_000_000, 0],
        [1, 0, 1_000],
    ]
)

(scipy.signal.convolve2d(data_int, conv) == wanted).sum()

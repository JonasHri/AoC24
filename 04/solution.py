# %%
import numpy as np
with open("input_04.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
data = [list(line) for line in data]
data = np.array(data)
# %%
leftright = [''.join(row) for row in data]
topbot = [''.join(row) for row in data.T]
norm_diag = [''.join(data.diagonal(i)) for i in range(-139, 140)]
rev_diag = [''.join(np.flip(data,axis=1).diagonal(i)) for i in range(-139, 140)]
all_rows = leftright + topbot + norm_diag + rev_diag
all_text = '|'.join(all_rows)

all_text.count('XMAS') + all_text[::-1].count('XMAS')
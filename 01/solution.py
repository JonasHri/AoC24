# %%
left = []
right = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left = sorted(left)
right = sorted(right)
left, right

diff = 0

for i in range(len(left)):
    diff += abs(left[i] - right[i])

diff

# %%
import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

count = 0
for line in data:
    # print(line.split())
    nums = [int(y) for y in line.split()]
    diffs = np.array([y - x for x, y in zip(nums, nums[1:])])
    if any(diffs == 0):
        continue
    if all(diffs > 0) and all(diffs <= 3):
        count += 1
    if all(diffs < 0) and all(diffs >= -3):
        count += 1
count

# %%
with open("input.txt", "r") as f:
    data = f.readlines()

reses, numses = [], []
for line in data:
    res, nums = line.split(":")
    res = int(res)
    nums = [int(x) for x in nums.split()]
    reses.append(res)
    numses.append(nums)


# %%

combs = []


def make_combs(rest, current):
    global combs
    if rest == 1:
        combs.append(current + "+")
        combs.append(current + "*")

    else:
        make_combs(rest - 1, current + "+")
        make_combs(rest - 1, current + "*")
    return


total = 0

test_w = 1

for res, nums in zip(reses, numses):
    combs = []
    make_combs(len(nums) - 1, "")
    for comb in combs:
        current = nums[0]

        for i, op in enumerate(comb):
            if op == "+":
                current += nums[i + 1]
            else:
                current *= nums[i + 1]
        if current == res:
            total += res
            break

total

# %%
import numpy as np
from copy import deepcopy

with open("input.txt", "r") as f:
    data = f.readlines()


starts = [int(x.strip()) for x in data]
starts


def mix(secret, other):
    return secret ^ other


def prune(secret):
    return secret % 16777216


def calculate_next(secret):
    res = secret * 64
    secret = mix(secret, res)
    secret = prune(secret)

    res = secret // 32
    secret = mix(secret, res)

    secret = prune(secret)

    res = secret * 2048
    secret = mix(secret, res)

    return prune(secret)


start = 123
for _ in range(10):
    start = calculate_next(start)
    print(start)

# %%

# starts = [1,10,100,2024]
total = 0
prices = []
changes = []

test_starts = [1, 2, 3, 2024]


for start in starts:
    secret = start
    secrets = [start] + [(secret := calculate_next(secret)) for i in range(2000)]

    prices.append([x % 10 for x in secrets])

    change = [x - y for x, y in zip(prices[-1], [0] + prices[-1])]
    change[0] = -99
    changes.append(change)

    total += secrets[-1]

total


prices = np.array(prices)
changes = np.array(changes)

# %% old
from time import perf_counter

proposal = np.array([-2, 1, -1, 3])
proposal = np.array([1, -3, 5, 1])
proposal = np.array([0, 0, -1, 2])

buy_at_old = dict()
start_time = perf_counter()
nanas = 0
for buyer_pos in range(len(prices)):
    for i in range(5, len(prices[0])):
        if (proposal == changes[buyer_pos, i - 4 : i]).all():
            # print(prices[buyer_pos, i], buyer_pos, i)
            buy_at_old[buyer_pos] = i
            nanas += prices[buyer_pos, i - 1]
            break

print(perf_counter() - start_time)

print(nanas)
# %%
m = 100

# changes[0,1:5] = proposal
single_changes = np.full_like(changes, -100)
for b in range(len(single_changes)):
    for i in range(5, len(single_changes[0])):
        change = changes[b, i - 4 : i]
        single_changes[b, i] = sum((change[i] + 9) * (m**i) for i in range(len(change)))

# single_changes[:, 3:] += (changes[:, :-3] + 9) * (100**0)
# single_changes[:, 3:] += (changes[:, 1:-2] + 9) * (100**1)
# single_changes[:, 3:] += (changes[:, 2:-1] + 9) * (100**2)
# single_changes[:, 3:] += (changes[:, 3:] + 9) * (100**3)
# single_changes[:, 3] = -1
# single_changes[:6,:6]

# %%
from time import perf_counter

proposal = np.array([1, -3, 5, 1])
proposal = np.array([-2, 1, -1, 3])

single_proposal = sum((proposal[i] + 9) * (m**i) for i in range(len(proposal)))

start_time = perf_counter()
nanas = 0
seen_buy = set()

buypoints = np.where(single_changes == single_proposal)

buy_at = dict()

for x, y in zip(buypoints[0], buypoints[1]):
    if x in seen_buy:
        continue
    seen_buy.add(x)
    buy_at[x] = y
    nanas += prices[x, y]


print(perf_counter() - start_time)

print(nanas)

# %%
for x, y in buy_at.items():
    print()
    print(x, y)
    print(changes[x, y - 4 : y])
    print(single_changes[x, y], prices[x, y - 1])
    poss = buypoints[1][np.where(buypoints[0] == x)]
    if min(poss) != y:
        print(x, y, poss)
        [3, 5][7]


# %%
from tqdm import tqdm

max_nanas = 0
for p1 in tqdm(range(-9, 10)):
    for p2 in range(-9, 10):
        for p3 in range(-9, 10):
            for p4 in range(-9, 10):
                proposal = np.array([p1, p2, p3, p4])

                single_proposal = sum((proposal[i] + 9) * (m**i) for i in range(len(proposal)))

                nanas = 0
                seen_buy = set()

                buypoints = np.where(single_changes == single_proposal)

                for x, y in zip(buypoints[0], buypoints[1]):
                    if x in seen_buy:
                        continue
                    seen_buy.add(x)
                    nanas += prices[x, y - 1]

                if nanas > max_nanas:
                    print(nanas, proposal)
                    max_nanas = nanas
max_nanas

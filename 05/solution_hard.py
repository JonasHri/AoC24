# %%
with open("input.txt", "r") as f:
    data = f.readlines()

rules = []

for line in data:
    if "|" in line:
        rule = line.split("|")
        rule = (int(rule[0]), int(rule[1]))
        rules.append(rule)
    else:
        break

updates = []

for line in data:
    if "," in line:
        pages = [int(page) for page in line.split(",")]
        updates.append(pages)

# %%
total = 0
for update in updates:
    correct = True
    for lower, higher in rules:
        if lower not in update or higher not in update:
            continue

        if update.index(lower) > update.index(higher):
            correct = False
            break

    if not correct:
        while not correct:
            correct = True
            for lower, higher in rules:
                if lower not in update or higher not in update:
                    continue

                l_index = update.index(lower)
                h_index = update.index(higher)
                if l_index < h_index:
                    pass
                else:
                    correct = False
                    repos = update.pop(l_index)
                    update.insert(h_index, repos)

        total += update[len(update) // 2]

total

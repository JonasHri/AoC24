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
rules

updates = []

for line in data:
    if "," in line:
        pages = [int(page) for page in line.split(",")]
        updates.append(pages)

updates
# %%
total = 0
for update in updates:
    correct = True
    for lower, higher in rules:
        try:
            if update.index(lower) > update.index(higher):
                correct = False
                break
        except:
            pass

    if correct:
        total += update[len(update) // 2]

total

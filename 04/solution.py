# %%
with open("input.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))
# %%
total = 0
total += "|".join(data).count("XMAS")
total += "|".join(data)[::-1].count("XMAS")
total

verts = []
for i in range(len(data)):
    vert = "".join([data[j][i] for j in range(len(data))])
    verts.append(vert)

total += "|".join(verts).count("XMAS")
total += "|".join(verts)[::-1].count("XMAS")


diags = []

for i in range(len(data)):
    diag_right = [data[j][i + j] for j in range(len(data) - i)]
    diag_left = [data[i + j][j] for j in range(1, len(data) - i)]
    diags.append(diag_left)
    diags.append(diag_right)

diags = list(map(lambda x: "".join(x), diags))
diags

total += "|".join(diags).count("XMAS")
total += "|".join(diags)[::-1].count("XMAS")
total

# %%
with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.strip() for x in data]

machines = []

add = 0
add = 10000000000000

for i in range(0, len(data), 4):
    a_button = data[i].split("+")
    ax, ay = int(a_button[-2].split(",")[0]), int(a_button[-1])

    b_button = data[i + 1].split("+")
    bx, by = int(b_button[-2].split(",")[0]), int(b_button[-1])

    prize = data[i + 2].split("=")
    px, py = int(prize[-2].split(",")[0]) + add, int(prize[-1]) + add

    machine = {
        "a": [ax, ay],
        "b": [bx, by],
        "prize": [px, py],
    }
    machines.append(machine)

machines
# %%
from pulp import LpProblem, LpVariable, LpConstraint, const

total = 0

for m in machines:
    prob = LpProblem("cost", const.LpMinimize)

    a = LpVariable("a", 0, None, const.LpInteger)
    b = LpVariable("b", 0, None, const.LpInteger)

    x_const = LpConstraint()

    prob += 3 * a + 1 * b, "Objective"

    # Define the constraints
    prob += m["a"][0] * a + m["b"][0] * b == m["prize"][0], "Constraint1"
    prob += m["a"][1] * a + m["b"][1] * b == m["prize"][1], "Constraint2"

    # Solve the problem
    status = prob.solve()
    if prob.status == 1:
        total += int(prob.objective.value())
        # print(f"Status: {prob.status}")
        # print(f"Optimal value of a: {a.varValue}")
        # print(f"Optimal value of b: {b.varValue}")
        # print(f"Objective value: {prob.objective.value()}")


total

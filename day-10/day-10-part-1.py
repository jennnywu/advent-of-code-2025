import re
from itertools import product

def popcount(x):
    return bin(x).count("1")

def solve_machine(target_bits, button_masks, n_lights):
    m = len(button_masks)
    rows = []

    for i in range(n_lights):
        row = 0

        for j, bm in enumerate(button_masks):
            if (bm >> i) & 1:
                row |= 1 << j

        rhs = (target_bits >> i) & 1
        rows.append([row, rhs])

    pivot_col = {}
    r = 0

    for c in range(m):
        pivot = None
        
        for i in range(r, n_lights):
            if (rows[i][0] >> c) & 1:
                pivot = i
                break

        if pivot is None:
            continue

        rows[r], rows[pivot] = rows[pivot], rows[r]
        pivot_col[r] = c

        for i in range(n_lights):
            if i != r and ((rows[i][0] >> c) & 1):
                rows[i][0] ^= rows[r][0]
                rows[i][1] ^= rows[r][1]

        r += 1

    for row, rhs in rows:
        if row == 0 and rhs == 1:
            return float("inf")
        
    p0 = 0

    for row_idx, col in pivot_col.items():
        if rows[row_idx][1]:
            p0 |= 1 << col

    free_cols = [c for c in range(m) if c not in pivot_col.values()]
    null_basis = []

    for fc in free_cols:
        vec = 1 << fc
        
        for row_idx, col in pivot_col.items():
            if (rows[row_idx][0] >> fc) & 1:
                vec |= 1 << col

        null_basis.append(vec)

    best = float("inf")

    for combo in product([0, 1], repeat = len(null_basis)):
        p = p0

        for bit, vec in zip(combo, null_basis):
            if bit:
                p ^= vec

        best = min(best, popcount(p))

    return best

count = 0

with open("day-10/input.txt") as f:
    input = f.read().splitlines()

for line in input:
    diagram = re.search(r"\[([.#]+)\]", line).group(1)
    n_lights = len(diagram)
    target_bits = 0

    for i, ch in enumerate(diagram):
        if ch == "#":
            target_bits |= 1 << i

    buttons = re.findall(r"\(([\d,]+)\)", line)
    button_masks = []

    for b in buttons:
        mask = 0

        for idx in map(int, b.split(",")):
            mask |= 1 << idx

        button_masks.append(mask)

    count += solve_machine(target_bits, button_masks, n_lights)

print(f"day 10 part 1: {count}")
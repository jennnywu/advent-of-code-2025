import re
from functools import lru_cache

def solve_machine_joltage(target, button_effects):
    k = len(target)
    target = tuple(target)
    effects = [tuple(eff) for eff in button_effects]
    masks = []

    for eff in effects:
        m = 0

        for i in eff:
            m |= 1 << i

        masks.append(m)

    affects = [[] for _ in range(k)]

    for j, m in enumerate(masks):
        for i in effects[j]:
            affects[i].append(j)

    for i, t in enumerate(target):
        if t > 0 and not affects[i]:
            return float("inf")

    def greedy_upper_bound(deficits):
        deficits = list(deficits)
        total = 0

        while True:
            if all(d == 0 for d in deficits):
                return total
            
            i = max(range(k), key=lambda x: deficits[x])

            if deficits[i] == 0:
                return total
            
            best_j = None
            best_score = -1

            for j in affects[i]:
                score = 0
                
                for c in effects[j]:
                    if deficits[c] > 0:
                        score += 1
                
                if score > best_score:
                    best_score = score
                    best_j = j
            
            for c in effects[best_j]:
                if deficits[c] > 0:
                    deficits[c] -= 1
            
            total += 1

    best = greedy_upper_bound(target)
    memo = {}
    stack = []
    stack.append((target, 0, None))

    while stack:
        deficits, base_cost, it = stack.pop()
        prev = memo.get(deficits)

        if prev is not None and prev <= base_cost:
            continue
        
        memo[deficits] = base_cost

        if deficits == (0,) * k:
            if base_cost < best:
                best = base_cost
            continue

        lb = max(deficits)

        if base_cost + lb >= best:
            continue

        i = max(range(k), key=lambda x: deficits[x])

        if deficits[i] == 0:
            if base_cost < best:
                best = base_cost
            continue

        cand = affects[i]
        cand = sorted(cand, key=lambda j: len(effects[j]), reverse=True)
        children = []

        for j in cand:
            max_press = min(deficits[c] for c in effects[j])
            xs = []

            for d in range(0, min(8, max_press + 1)):
                xs.append(max_press - d)
            if 0 not in xs:
                xs.append(0)

            xs = sorted(set(x for x in xs if x >= 0), reverse=True)

            for x in xs:
                if x == 0:
                    continue

                nd = list(deficits)
                for c in effects[j]:
                    nd[c] -= x
                nd = tuple(nd)

                if base_cost + x + max(nd) >= best:
                    continue

                children.append((nd, base_cost + x, None))

        if not children:
            for j in cand:
                nd = list(deficits)

                for c in effects[j]:
                    if nd[c] > 0:
                        nd[c] -= 1

                nd = tuple(nd)

                if nd == deficits:
                    continue
                if base_cost + 1 + max(nd) >= best:
                    continue
                
                children.append((nd, base_cost + 1, None))

        for child in reversed(children):
            stack.append(child)

    return best

def parse_line(line):
    target = tuple(map(int, re.search(r"\{([\d,]+)\}", line).group(1).split(",")))
    buttons = re.findall(r"\(([\d,]+)\)", line)
    button_effects = [tuple(map(int, b.split(","))) for b in buttons]
    button_effects.sort(key=len, reverse=True)
    
    return target, button_effects

def solve_all(path="day-10/input.txt"):
    total = 0
    
    with open(path) as f:
        for line in f:
            
            line = line.strip()
            
            if not line:
                continue
            
            target, button_effects = parse_line(line)
            total += solve_machine_joltage(target, button_effects)
    
    return total

if __name__ == "__main__":
    print("day 10 part 2:", solve_all())
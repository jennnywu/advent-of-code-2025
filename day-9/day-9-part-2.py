with open("day-9/input.txt") as f:
    red = [tuple(map(int, line.split(","))) for line in f if line.strip()]

n = len(red)

vertical_edges = []
for i in range(n):
    x1, y1 = red[i]
    x2, y2 = red[(i + 1) % n]
    if x1 == x2:
        vertical_edges.append((x1, min(y1, y2), max(y1, y2)))

xs = set()
ys = set()

for x, y in red:
    xs.add(x)
    xs.add(x + 1)
    ys.add(y)
    ys.add(y + 1)

min_rx = min(x for x, _ in red)
max_rx = max(x for x, _ in red)
min_ry = min(y for _, y in red)
max_ry = max(y for _, y in red)

xs.add(min_rx - 1)
xs.add(max_rx + 2)
ys.add(min_ry - 1)
ys.add(max_ry + 2)

xs = sorted(xs)
ys = sorted(ys)

x_id = {x: i for i, x in enumerate(xs)}
y_id = {y: i for i, y in enumerate(ys)}

W = len(xs) - 1
H = len(ys) - 1

interior = [[False] * W for _ in range(H)]

for j in range(H):
    y_mid = (ys[j] + ys[j + 1]) / 2.0
    hits = []

    for x, ymin, ymax in vertical_edges:
        if ymin <= y_mid < ymax:
            hits.append(x)

    hits.sort()

    for k in range(0, len(hits), 2):
        if k + 1 >= len(hits):
            break
        
        xl = hits[k]
        xr = hits[k + 1]
        iL = x_id[xl]
        iR = x_id[xr]
        
        for i in range(iL, iR):
            interior[j][i] = True

boundary = [[False] * W for _ in range(H)]

for k in range(n):
    x1, y1 = red[k]
    x2, y2 = red[(k + 1) % n]

    if x1 == x2:
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        ix = x_id[x1]

        for j in range(H):
            if ys[j] >= ymin and ys[j + 1] <= ymax:
                boundary[j][ix] = True

    else:
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        iy = y_id[y1]

        for i in range(W):
            if xs[i] >= xmin and xs[i + 1] <= xmax:
                boundary[iy][i] = True

allowed = [[False] * W for _ in range(H)]

for j in range(H):
    for i in range(W):
        allowed[j][i] = interior[j][i] or boundary[j][i]

ps = [[0] * (W + 1) for _ in range(H + 1)]

for j in range(H):
    cell_h = ys[j + 1] - ys[j]
    
    for i in range(W):
        cell_w = xs[i + 1] - xs[i]
        ps[j + 1][i + 1] = (
            (cell_w * cell_h if allowed[j][i] else 0)
            + ps[j][i + 1]
            + ps[j + 1][i]
            - ps[j][i]
        )

def rect_sum(ix0, iy0, ix1, iy1):
    return (
        ps[iy1][ix1]
        - ps[iy0][ix1]
        - ps[iy1][ix0]
        + ps[iy0][ix0]
    )

max_area = 0

for i in range(n):
    x1, y1 = red[i]
    
    for j in range(i + 1, n):
        x2, y2 = red[j]

        if x1 == x2 or y1 == y2:
            continue

        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        
        if area <= max_area:
            continue

        ix0 = x_id[x_min]
        ix1 = x_id[x_max + 1]
        iy0 = y_id[y_min]
        iy1 = y_id[y_max + 1]

        if rect_sum(ix0, iy0, ix1, iy1) == area:
            max_area = area

print(f"day 9 part 2: {max_area}")
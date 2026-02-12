import math

W, H, sx, sy, ex, ey = map(int, input().split())

grid = []
for _ in range(H // 2):
    grid.append(list(map(int, input().split())))
# (x, y) coordinates of central points correspond to grid[y // 2][x // 2],
# so we transpose the grid to simplify indexing
grid = [[grid[j][i] for j in range(H // 2)] for i in range(W // 2)]

# equation of the path segment: (y - sy)(ex - sx) = (x - sx)(ey - sy)
intersections = set()
eps = 1e-6
xdir = 1 if sx <= ex else -1
for x in range(sx + xdir, ex + xdir, 2 * xdir):
    y = sy + (ey - sy) / (ex - sx) * (x - sx)
    if abs(y - round(y)) < eps:   # round to integer
        y = round(y)
    intersections.add((x, y))
ydir = 1 if sy <= ey else -1
for y in range(sy + ydir, ey + ydir, 2 * ydir):
    x = sx + (ex - sx) / (ey - sy) * (y - sy)
    if abs(x - round(x)) < eps:   # round to integer
        x = round(x)
    intersections.add((x, y))

total_length = math.sqrt((ex - sx) ** 2 + (ey - sy) ** 2)

for x, y in intersections:
    if (x / 2).is_integer() and (y / 2).is_integer():
        roof_prev = grid[(x - xdir) // 2][(y - ydir) // 2]
        roof_next = grid[(x + xdir) // 2][(y + ydir) // 2]
        roof_box3 = grid[(x - xdir) // 2][(y + ydir) // 2]
        roof_box4 = grid[(x + xdir) // 2][(y - ydir) // 2]

        second_max = sorted([roof_prev, roof_next, roof_box3, roof_box4])[2]
        total_length += abs(second_max - roof_prev) + abs(second_max - roof_next)

    elif (x / 2).is_integer():
        y = round(y - (y % 2) + 1)
        roof_next = grid[(x + xdir) // 2][y // 2]
        roof_prev = grid[(x - xdir) // 2][y // 2]

        total_length += abs(roof_next - roof_prev)

    else:
        x = round(x - (x % 2) + 1)
        roof_prev = grid[x // 2][(y - ydir) // 2]
        roof_next = grid[x // 2][(y + ydir) // 2]

        total_length += abs(roof_next - roof_prev)

print(total_length)
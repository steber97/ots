def first_spot_in_ray(r0, c0, grid, dr, dc, single=False):
    r, c = r0 + dr, c0 + dc
    while r < len(grid) and 0 <= c < len(grid[0]):
        if grid[r][c] >= 0:
            return grid[r][c]
        if single:
            break
        r += dr
        c += dc
    return -1

def first_connections(spots, grid, type):
    moves = {
        'K': ([(0, 1), (1, -1), (1, 0), (1, 1)], True),
        'Q': ([(0, 1), (1, -1), (1, 0), (1, 1)], False),
        'R': ([(0, 1), (1, 0)], False),
        'B': ([(1, -1), (1, 1)], False),
        'N': ([(1, -2), (1, 2), (2, -1), (2, 1)], True),
    }
    dirs, single = moves[type]

    graph = []
    for k, (r0, c0) in enumerate(spots):
        for dr, dc in dirs:
            h = first_spot_in_ray(r0, c0, grid, dr, dc, single=single)
            if h != -1:
                graph.append((k, h))
    return graph

def find(i, par):
    if par[i] == i:
        return i
    par[i] = find(par[i], par)
    return par[i]

def union(i, j, par):
    pi = find(i, par)
    pj = find(j, par)
    if pi == pj:
        return False
    par[pj] = pi
    return True


n, type = input().split()
n = int(n)

spots = []
grid = [[-1 for _ in range(n)] for _ in range(n)]
k = 0
for r in range(n):
    chars = input().strip()
    for c, ch in enumerate(chars):
        if ch != '.':
            spots.append((r, c))
            grid[r][c] = k
            k += 1
m = len(spots)

# Create the graph using only first connections
graph = first_connections(spots, grid, type)

# Create the forest and check connectivity
par = [k for k in range(m)]
adj = [set() for _ in range(m)]
for i, j in graph:
    if union(i, j, par):
        adj[i].add(j)
        adj[j].add(i)

connected = True
for k in range(1, m):
    if find(k, par) != find(k - 1, par):
        connected = False
        break

# Reduce the tree leaf by leaf
if connected:
    print("YES")
    leaves = [k for k in range(m) if len(adj[k]) == 1]
    while len(leaves) >= 2:
        i = leaves.pop(-1)
        j = adj[i].pop()
        print(f"{spots[i][0] + 1} {spots[i][1] + 1} "
              f"{spots[j][0] + 1} {spots[j][1] + 1}")
        adj[j].remove(i)
        if len(adj[j]) == 1:
            leaves.append(j)
else:
    print("NO")

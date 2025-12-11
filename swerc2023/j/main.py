def bfs(a, g, dist, col):
    dist[0][a][a] = 0
    queue = [(a, 0)]
    while len(queue) > 0:
        v, parity = queue.pop(0)
        for u in g[v]:
            if col[u] == col[v]:
                if dist[parity][a][v] + 1 < dist[parity][a][u]:
                    dist[parity][a][u] = dist[parity][a][v] + 1
                    queue.append((u, parity))
            else:
                if dist[parity][a][v] + 1 < dist[(1 - parity)][a][u]:
                    dist[(1 - parity)][a][u] = dist[parity][a][v] + 1
                    queue.append((u, (1 - parity)))


n, m, k = map(int, input().split())
col = list(map(int, input().strip().split()))

g = [[] for _ in range(n)]
for e in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist = [[[n + k + 3 for _ in range(n)] for _ in range(n)] for _ in [0, 1]]
for a in range(n):
    bfs(a, g, dist, col)

res = 0
for a in range(n):
    for b in range(a + 1, n):
        i = (k + dist[1][a][b] - dist[0][a][b]) // 2
        i = max(0, i)
        i = min(k, i)
        d = min(dist[0][a][b] + i, dist[1][a][b] + k - i)
        res = max(res, d)

print(res)

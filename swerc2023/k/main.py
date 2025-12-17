t = int(input())

for _ in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)

    degrees = [0]*n
    edges = []
    companies = []
    for _ in range(m):
        a, b = input().split()
        a, b = int(a)-1, int(b)-1
        degrees[a] += 1
        degrees[b] += 1
        edges.append(sorted((a, b)))
    if m == (n*(n-1)) // 2:
        print(3)
        for a, b in edges:
            if a == 0 and b == 1:
                companies.append('1')
            elif a == 0:
                companies.append('2')
            else:
                companies.append('3')
    else:
        fixed_node = None
        print(2)
        for node in range(n):
            if degrees[node] != n-1:
                fixed_node = node
                break
        for a, b in edges:
            if a == fixed_node or b == fixed_node:
                companies.append('1')
            else:
                companies.append('2')
    print(" ".join(companies))
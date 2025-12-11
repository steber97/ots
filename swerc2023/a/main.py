t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.append(1440)

    walks = 0
    curr_time = 0
    for i in range(n + 1):
        delta = a[i] - curr_time
        curr_time = a[i]
        if delta >= 240:
            walks += 2
        elif delta >= 120:
            walks += 1
        if walks >= 2:
            break

    if walks >= 2:
        print("YES")
    else:
        print("NO")

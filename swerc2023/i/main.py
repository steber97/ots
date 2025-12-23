def bernardo(n, m, x, k):
    print("Bernardo", flush=True)
    for i in range(n):
        y, a = [int(l) for l in input().rstrip().split()]
        if y - 1e-6 > m/k:
            for b in range(a, a+y):
                if b % ((m//k) + 1) == 0:
                    print(b, flush=True)
                    break
        else:
            print(a, flush = True)


def alessia(n, m, x):
    print("Alessia", flush=True)
    bernardos = [0, m+1]
    for i in range(n):
        for j in range(len(bernardos)-1):
            if x[i] + bernardos[j] + 1 <= bernardos[j+1]:
                print(x[i], bernardos[j]+1, flush=True)
                break
        b = int(input().rstrip())
        # print(b, "debug")
        bernardos.append(b)
        bernardos = sorted(bernardos)



n, m = [int(x) for x in input().rstrip().split()]
x = [int(x) for x in input().rstrip().split()]

x = sorted(x, reverse=True)
played = False
for k in range(1, n+1):
    if m / k + 1e-6 < x[k-1] and not played and n > 1:
        bernardo(n, m, x, k)
        played = True
if not played:
    alessia(n, m, x)
import sys

def modinv(n, M):
    inv = [0] * (n + 2)
    inv[1] = 1
    for i in range(2, n + 2):
        inv[i] = M - (M // i) * inv[M % i] % M
    return inv

def catalan(n):
    inv = modinv(n, M)
    C = [0] * (n + 1)
    C[0] = 1

    c = 1
    for i in range(1, n + 1):
        c = c * 2 * (2 * i - 1) % M
        c = c * inv[i + 1] % M
        C[i] = c

    return C


M = 1_000_000_007

# speed up input reading
data = sys.stdin.read().split()
N = int(data[0])
E = list(map(int, data[1:]))

res = 1
stak = [-1]   # simplifies the code to handle s[-1] at the beginning
E.append(-1)   # simplifies the code to empty the stack at the end
levels = []
max_level = 0
for e in E:
    last = stak[-1]
    k = 0
    while e < stak[-1]:
        h = stak.pop()
        if h == last:
            k += 1
        else:
            levels.append(k)
            k = 1
            last = h
    levels.append(k)
    stak.append(e)

max_level = max(levels)
C = catalan(max_level)
for l in levels:
    res = res * C[l] % M

print(res)

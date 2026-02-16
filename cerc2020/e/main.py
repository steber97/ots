import math


def create_gadget(k, delay, base, cuts, harvests):
    for i in range(k + 1):
        for j in range(i + 1):
            cuts.append((j, base + i - j, 0))
    for i in range(-1, -delay, -1):
        cuts.append((i, base, 0))
    cuts.append((-delay, base, 1))

    for j in range(k + 1):
        harvests.append((j, base + k - j))

    return cuts, harvests


n = int(input())

days = math.floor(math.log2(n)) + 1 if n != 0 else 0
cuts = []
harvests = []
k = 0
base = 0
while n > 0:
    if n % 2 != 0:
        create_gadget(k, days - k, base, cuts, harvests)
        base += k + 3
    k += 1
    n = n // 2

print(len(cuts))
for c0, c1, c2 in cuts:
    print(c0, c1, c2)
print(len(harvests), days)
for h0, h1 in harvests:
    print(h0, h1)

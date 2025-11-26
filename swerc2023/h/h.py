def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
s = input()
p = s.count('+')
m = s.count('-')
assert m + p == n

q = int(input())
for _ in range(int(q)):
    a, b = map(int, input().split())
    d = gcd(a, b)
    aa, bb = a // d, b // d

    if aa == bb:
        print("YES" if p == m else "NO")
        continue

    if (p - m) % (bb - aa) == 0:
        k = (p - m) // (bb - aa)
        if k >= 0:
            print("YES" if (p >= k * bb and m >= k * aa) else "NO")
        else:
            print("YES" if (m >= -k * bb and p >= -k * aa) else "NO")
    else:
        print("NO")

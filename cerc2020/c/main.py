import math


if __name__ == "__main__":
    n = int(input())
    street = input()
    L = int(input())
    values = {}
    M = 0
    for l in range(L):
        let, val = input().split()
        val = int(val)
        values[let] = val
        M = max(M, val)
    p = 1
    K = 0
    for i in range(2, n+1):
        if n % i == 0:
            p = i
            for k in range(n):
                if p**k == n:
                    K = k
                    break
            break
    assert n == p**K

    maxval = 0
    DP = []
    for s in range(0, K+1):
        DP.append([])
        for start in range(0, (p**s)):
            DP[-1].append(0)
    for i in range(0, n):
        DP[K][i] = M if street[i] == '?' else values[street[i]]
    
    for s in range(K-1, -1, -1):
        k = K - s
        for start in range(0, (p**s)):
            total = 0
            already_seen = None
            count = True
            for i in range(start, n, p**s):
                if street[i] != '?':
                    if already_seen is None:
                        already_seen = street[i]
                    elif already_seen != street[i]:
                        count = False
            if count:
                if already_seen is None:
                    total = (k+1) * (p**k) * M
                else:
                    total = (k+1) * (p**k) * values[already_seen]
        
            DP[s][start] = max(
                total,
                sum([DP[s+1][j * p**s + start] for j in range(0,p)]))
    
    print(DP[0][0])
            
                
            


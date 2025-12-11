n = int(input())
wines = [w for w in input().strip()]

max_count = 0
for i in range(n):
    if wines[i] == 'W':
        max_count += 1

curr_count = max_count
for i in range (n - 1):
    curr_count += 1 if wines[n + i] == 'W' else 0
    curr_count -= 1 if wines[i] == 'W' else 0
    if curr_count > max_count:
        max_count = curr_count
print(max_count)

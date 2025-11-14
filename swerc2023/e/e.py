# dictionary:   key:     idx,
#               value:   [(x, y), prev_idx, next_idx, slice_area]
points = {}


def compute_slice(idx: int):
    xx, yy = points[idx][0]
    prev_idx = points[idx][1]
    next_idx = points[idx][2]
    xa, ya = points[prev_idx][0]
    xb, yb = points[next_idx][0]

    return abs(xx*ya + xa*yb + xb*yy - yy*xa - ya*xb - yb*xx)


def update(choice: int):
    idx = choice - 1
    prev_idx = points[idx][1]
    next_idx = points[idx][2]
    points[prev_idx][2] = next_idx
    points[next_idx][1] = prev_idx
    points.pop(idx)
    points[prev_idx][3] = compute_slice(prev_idx)
    points[next_idx][3] = compute_slice(next_idx)


def choose():
    min_size = float('inf')
    min_idx = -1
    for i in points:
        if points[i][3] < min_size:
            min_size = points[i][3]
            min_idx = i
    choice = min_idx + 1
    return choice


def my_move():
    choice = choose()
    print(choice, flush=True)
    update(choice)


def other_move():
    choice = int(input())
    update(choice)



n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    points[i] = [(x, y), i-1, i+1, 0]
points[0][1] = n-1
points[n-1][2] = 0

for i in range(n):
    points[i][3] = compute_slice(i)

if n % 2 == 0:
    print("Alberto", flush=True)
else:
    print("Beatrice", flush=True)
    other_move()

while len(points) >= 4:
    my_move()
    other_move()

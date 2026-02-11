import math

W, H, start_x, start_y, end_x, end_y = map(int, input().split())
grid = []
for _ in range(H//2):
    grid.append(list(map(int, input().split())))

grid = [[grid[j][i] for j in range(H//2)] for i in range(W//2)]

# equation of the path segment: (y - s_y)(e_x - s_x) = (x - s_x)(e_y - s_y)
intersections = set()
vert_step = 2 if start_x < end_x else -2
for vertical in range(start_x + vert_step //2, end_x + vert_step//2, vert_step):
    intersections.add((vertical, start_y + (end_y - start_y)/(end_x - start_x)* (vertical - start_x)))

#hor_intersections = set()
hor_step = 2 if start_y < end_y else -2
for hor in range(start_y + hor_step//2, end_y + hor_step//2, hor_step):
    intersections.add((start_x + (end_x - start_x)/(end_y - start_y)* (hor - start_y), hor))

total_length = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)

for point in intersections:
    if (point[0]/2).is_integer() and (point[1]/2).is_integer():
        #  We have a multiple intersection
        print(f"We are at point {point}")
        height_prev = grid[round((point[0] - vert_step//2)//2)][round((point[1] - hor_step//2)//2)]
        height_next = grid[round((point[0] + vert_step//2)//2)][round((point[1] + hor_step//2)//2)]
        height_neighbor1 = grid[round((point[0] - vert_step // 2) // 2)][round((point[1] + hor_step // 2) // 2)]
        height_neighbor2 = grid[round((point[0] + vert_step // 2) // 2)][round((point[1] - hor_step // 2) // 2)]

        second_max = sorted([height_prev, height_next, height_neighbor1, height_neighbor2])[2]
        total_length += abs(second_max - height_prev) + abs(second_max - height_next)

    elif (point[0]/2).is_integer():
        height_prev = grid[round((point[0] - vert_step // 2) // 2)][round((point[1] - (point[1] % 2) + 1) //2)]
        height_next = grid[round((point[0] + vert_step // 2) // 2)][round((point[1] - (point[1] % 2) + 1) //2)]

        total_length += abs(height_prev - height_next)

    else:
        height_prev = grid[round((point[0] - (point[0] % 2) + 1) // 2)][round((point[1] - hor_step // 2) // 2)]
        height_next = grid[round((point[0] - (point[0] % 2) + 1) // 2)][round((point[1] + hor_step // 2) // 2)]

        total_length += abs(height_prev - height_next)

print(total_length)
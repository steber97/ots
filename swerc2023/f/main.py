inpt = input()
num_cases = int(inpt)

for _ in range(1, num_cases + 1):
    n = int(input())
    find_array = input().rstrip('\n').split()
    target_array = input().rstrip('\n').split()

    find_ind = n-1
    curr_ind = n-1
    while curr_ind > -1:
        # We find target_array[curr_ind] in find_array
        while find_ind > -1 and find_array[find_ind] != target_array[curr_ind]:
            find_ind -= 1
        if find_ind == -1:
            print(curr_ind+1)
            break
        curr_ind -= 1
    if curr_ind == -1:
        print(0)
import math, collections
'''
[1, 0, 0]
[1, 0, 0]
[1, 9, 0]

[1,0,1,1,1]
[1,0,1,1,1]
[1,1,1,0,1]
[0,0,0,0,9]

[1, 1, 1, 1, 1, 1, 1 ,1, 1]
[1, 1, 1, 1, 1, 1, 1 ,1, 1]
[1, 1, 0, 1, 1, 1, 1 ,1, 1]
[1, 1, 1, 1, 1, 1, 1 ,1, 1]
[1, 1, 1, 1, 1, 1, 0 ,1, 1]
[1, 0, 1, 1, 1, 1, 1 ,1, 1]
[1, 1, 1, 1, 1, 1, 0 ,1, 9]
'''
def print_map(arr):
    for i in arr:
        print(i)
    print('----------')

def is_valid(j, i, row, col):
    return i >= 0 and i < col and j >= 0 and j < row

def minimumDistance(area):
    # Write your code here
    row, col = len(area), len(area[0])
    q = collections.deque([[0, 0]])
    visit = []

    curr_step = 0
    while q:
        for _ in range(len(q)):
            [j, i] = q.popleft()

            if not is_valid(j, i, row, col) or area[j][i] == 0 or [j, i] in visit:
                continue
            
            if area[j][i] == 9:
                return curr_step
            visit.append([j, i])
            area[j][i] = curr_step

            print("visit: ", visit)
            print_map(area)

            q.append([j + 1, i])
            q.append([j - 1, i])
            q.append([j, i + 1])
            q.append([j, i - 1])

        curr_step += 1
            
    
    return -1



area = [[1, 0, 0], [1, 0, 0], [1, 9, 0]]
area1 = [[1,0,1,1,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,9]]
area2 = [[1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 0, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 0 ,1, 1], [1, 0, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 0 ,1, 9]]
print(minimumDistance(area2))


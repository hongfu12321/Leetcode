import math

def print_map(arr):
    for i in arr:
        print(i)
    print('----------')

def minimumDistance(area):
    # Write your code here
    print_map(area)
    col = len(area)
    row = len(area[0])
    des = []
    
    for i, arr in enumerate(area):
        for j, num in enumerate(arr):
            if num == 9:
                dest = [i, j]
    # print(dest)
    
    new_map = []
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(0)
        new_map.append(tmp)
    new_map[0][0] = 1
    # print_map(new_map)
    # print('---------')
    
    def helper(cur, i, j, pre):
        if i >= len(area) or i < 0 or j >= len(area[0]) or j < 0: return
        if new_map[i][j] == -1: return
        # print('---', i, j, pre)
        
        if area[i][j] == 1 or area[i][j] == 9:
            if new_map[i][j] == 0 or cur < new_map[i][j]:
                new_map[i][j] = cur
            elif new_map[i][j] == 1:
                pass
            else:
                return
        else:
            new_map[i][j] = -1
        
        # print_map(new_map)
        if new_map[i][j] == -1: return 
        if pre != [1, 0]: helper(new_map[i][j] + 1, i + 1, j, [-1, 0])
        if pre != [-1, 0]:helper(new_map[i][j] + 1, i - 1, j, [1, 0])
        if pre != [0, 1]:helper(new_map[i][j] + 1, i, j + 1, [0, -1])
        if pre != [0, -1]:helper(new_map[i][j] + 1, i, j - 1, [0, 1])
        
    
    helper(1, 0, 0, [0, 0])
    print_map(new_map)

    return new_map[dest[0]][dest[1]] - 1


area = [[1, 0, 0], [1, 0, 0], [1, 9, 0]]
area1 = [[1,0,1,1,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,9]]
area2 = [[1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 0, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 0 ,1, 1], [1, 0, 1, 1, 1, 1, 1 ,1, 1], [1, 1, 1, 1, 1, 1, 0 ,1, 9]]
print(minimumDistance(area2))


# BFS
def bfs(root, match):
    queue = collections.deque([root])
    # 記錄層數
    steps = 0
    # 返回的答案
    ans = []
    # 隊列不空，生命不止！
    while queue:
        size = len(queue)
        # 遍歷此層所有的節點
        for _ in range(size):
            queue.popleft()
            if step == match: ans.append(node)
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
        # 遍歷完當前層，層數+1
        steps += 1

    return ans


# if we don't need to mark the step
def bfs(root, condition):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node == condition: return node
        if node.right: queue.append(node.right)
        if node.left: queue.append(node.left)

    return -1




# DFS
def dfs(root: TreeNode):
    if (MATCH): return RESULT
    dfs(root.left)
    dfs(root.right)


def dfs(root):
    stack = []      
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ####
        #Main logic here!!
        ####
        root = root.right
    return -1
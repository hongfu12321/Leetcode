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


def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)


def maxDepth(node):
    if not node: return 0

    return max(maxDepth(node.left), maxDepth(node.right)) + 1

def getMaxWidth(root):
    # base case
    if root is None:
        return 0
  
    q = collections.deque([root])
    maxWidth = 0
  
    while (q != []):
        # Get the size of queue when the level order
        # traversal for one level finishes
        count = len(q)
  
        # Update the maximum node count value
        maxWidth = max(count, maxWidth)
  
        while (count is not 0):
            count = count-1
            temp = q[-1]
            q.pop()
            if temp.left is not None:
                q.insert(0, temp.left)
  
            if temp.right is not None:
                q.insert(0, temp.right)
  
    return maxWidth
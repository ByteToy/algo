from typing import Optional
# deque是collections中的双向链表实现
from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# 使用递归方式，将list转换为二叉树，按层的顺序实现转换
# 先判断arr的下标start是否越界，然后再新建节点
def create_btree(arr, start):
    if start < 0 or start >= len(arr) or arr[start] is None:
        return None
    root = TreeNode(arr[start])
    root.left = create_btree(arr, start * 2 + 1)
    root.right = create_btree(arr, start * 2 + 2)

    return root


# 广度优先（breadth-first traversal）方式遍历二叉树
# 以队列方式实现，按层进行遍历
def bfs_travel(root):
    res = []
    queue = deque()
    queue.append(root)
    while queue:
        node: TreeNode = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

res_pre=[]
# 深度优先就是使用递归方式
# 深度优先（depth-first search）：前序遍历
# 前序遍历：根节点-左子树-右子树
# 中序遍历：左子树-根节点-右子树
# 后续遍历：左子树-右子树-根节点
def dfs_pre(root:TreeNode):
    # 递归边界（返回条件）：节点为None
    if root is None:
        return
    # 访问根节点
    res_pre.append(root.val)
    # 递归处理左子树
    dfs_pre(root=root.left)
    # 递归处理右子树
    dfs_pre(root=root.right)

res_mid=[]
# 深度优先遍历：中序方式，左子树-根节点-右子树
# 如果是一个有序的二叉树，中序遍历出来的元素就是一个有序的列表，左节点< 中节点（根节点） < 右节点
def dfs_mid(root:TreeNode):
    if root is None:
        return
    dfs_mid(root=root.left)
    res_mid.append(root.val)
    dfs_mid(root=root.right)



if __name__ == "__main__":
    arr = [5, 9, 11, 15, 18, 90, 243, 2, 55]
    root = create_btree(arr, 0)
    cur=root
    while cur is not None:
        print(cur.val,end='\t')
        cur=cur.left
    print()
    print('广度优先遍历：',bfs_travel(root))
    dfs_pre(root)
    print('深度优先遍历-前序：',res_pre)
    dfs_mid(root)
    print('深度优先遍历-中序：',res_mid)

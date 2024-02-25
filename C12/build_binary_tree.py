from collections import deque
# 分治算法应用：
# 构建二叉树
# 根据深度优先前序遍历列表和中序遍历列表，还原二叉树

# 树节点类
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None

# 以深度优先的方式构建二叉树
# 使用递归的分治策略，根据前序列表和中序字典，逐层向下递归，向上返回的方式构建二叉树，可以通过return上部的print查看构建过程
# 参数说明：
# pre_list:深度优先前序遍历列表
# mid_dict:深度优先中序遍历列表生成的列表
# root_index:前序列表中根节点下标
# left:中序列表左侧元素下标
# right:中序列表右侧元素下标
def dfs(pre_list:list[int],mid_dict:dict[int,int],root_index,left,right):
    # 当前节点为叶子节点，right和left指向同一个节点
    if right-left<0:
        return None
    root=TreeNode(pre_list[root_index])
    # 通过前序列表元素值，在中序列表中获取下标
    t=mid_dict[pre_list[root_index]]
    root.left=dfs(pre_list,mid_dict,root_index+1,left,t-1)
    root.right=dfs(pre_list,mid_dict,root_index+1+t-left,t+1,right)
    print(bfs_travel(root))
    return root


def build_tree(pre_list: list[int], mid_list: list[int]):
    # 将列表转换为字典，且将列表的值作为健，下标作为键值，后续需要通过键值查找到列表的下标，此下标即为m，用于后续计算左右子节点的首尾下标，以及右子树根节点下标
    mid_dict = {val: index for index, val in enumerate(mid_list)}
    root=dfs(pre_list,mid_dict,0,0,len(pre_list)-1)
    return root

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

if __name__ == '__main__':
    # bfs_list = [5, 9, 11, 15, 18, 90, 243, 2, 55]
    pre_list = [5, 9, 15, 2, 55, 18, 11, 90, 243]
    mid_list = [2, 15, 55, 9, 18, 5, 90, 11, 243]
    root=build_tree(pre_list,mid_list)
    res=bfs_travel(root)
    print(res)

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTreeSearch:
    def __init__(self):
        self.__root: TreeNode = None
        self.__res=[]

    # 广度优先遍历
    def bfs(self):
        self.__res=[]
        queue = deque()
        queue.append(self.__root)
        while queue:
            node: TreeNode = queue.popleft()
            self.__res.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return self.__res

    # 深度优先搜索
    # 这一段是看了别人的写法，很有意思
    # 注意if判断的位置和含义
    def dfs(self,node,order):
        cur = node
        if node is None:
            return
        if order=='pre':
            self.__res.append(cur.val)
        self.dfs(cur.left,order)
        if order=='mid':
            self.__res.append(cur.val)
        self.dfs(cur.right,order)
        if order=='post':
            self.__res.append(cur.val)

    # 深度优先遍历-中序
    # 中序遍历，应该返回一个有序的列表
    def dfs_mid(self):
        cur=self.__root
        self.__res=[]
        self.dfs(cur,'mid')
        return self.__res

    def dfs_pre(self):
        cur=self.__root
        self.__res=[]
        self.dfs(cur,'pre')
        return self.__res

    # 当value> 当前节点，跳至当前节点的右子节点
    # 当value< 当前节点，跳至当前节点的左子节点
    # 在while循环中，如果相等则返回True，如果while循环结束仍未跳出循环，说明未找到，则在while循环外返回False
    def search(self, value)->bool:
        cur = self.__root
        while cur is not None:
            if cur.val < value:
                cur = cur.right
            elif cur.val > value:
                cur = cur.left
            else:
                return True
        return False

    # 考虑两种情况，数为空None和非空，为空则建立一个新节点，然后root指向即可
    # 树非空时，则根据搜索的原理，沿着路径向下走，直到空节点（cur），此时pre为父节点
    # 判断value与pre节点的大小，然后在左右插入节点。
    def insert(self, value):
        if self.__root is None:
            self.__root=TreeNode(value)
            return
        cur=self.__root
        pre=None
        while cur is not None:
            if cur.val==value:
                return
            pre=cur
            if cur.val<value:
                cur=cur.right
            else:
                cur=cur.left

        node=TreeNode(value)
        if pre.val<value:
            pre.right=node
        else:
            pre.left=node

    # 删除元素，删除成功返回True，失败返回False
    def remove(self,value)->bool:
        # 首先判断树是否为空
        if self.__root is None:
            return False
        cur=self.__root
        pre=None

        # 遍历二叉树，查找待删除的元素
        # 找到元素跳出循环，否则继续循环，直到二叉树遍历结束
        # 注：如果未找到元素，此时cur=None，找到元素时，cur=该元素，而pre则为父节点
        while cur is not None:
            if cur.val==value:
                break
            pre=cur
            if cur.val<value:
                cur=cur.right
            else:
                cur=cur.left

        # 遍历结束仍未找到要删除的元素
        if cur is None:
            return False
        # 找到待删除的节点，判断节点子节点的个数
        # 有0、1个子节点时
        if cur.left is None or cur.right is None:
            # 获取叶子节点
            child=cur.left or cur.right
            if cur!=self.__root:
                if pre.left==cur:
                    pre.left=child
                else:
                    pre.right=child
            else:
                self.__root=child
        # 有2个子节点时，这里是将右子树最小节点代替删除节点内容
        else:
            tmp=cur.right
            # 退出while循环时，tmp位于子树最左侧节点，即最小节点
            while tmp.left is not None:
                tmp=tmp.left
            # 此时tmp为叶子节点，直接删除即可。
            self.remove(tmp.val)
            cur.val=tmp.val
        return True


if __name__ == "__main__":
    arr = [15,9,90,5,11,55,243]
    bts=BinaryTreeSearch()
    for val in arr:
        bts.insert(val)
    bts.insert(2)
    bts.insert(65)
    print('广度优先遍历：',bts.bfs())
    print('搜索一个元素：',bts.search(55))
    print('深度优先搜索-中序：',bts.dfs_mid())
    print('深度优先遍历-前序',bts.dfs_pre())
    print(bts.remove(9))
    print('2.广度优先遍历：', bts.bfs())
    print('2.深度优先搜索-中序：', bts.dfs_mid())

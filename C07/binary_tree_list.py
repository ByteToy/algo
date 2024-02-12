class BinaryTreeList:
    def __init__(self, arr):
        self.__tree = list(arr)
        self.__res = []

    def size(self):
        return len(self.__tree)

    # 注：是>=
    def getVar(self, i):
        if i < 0 or i >= self.size():
            return None
        return self.__tree[i]

    def getLeft(self, i):
        return i * 2 + 1

    def getRight(self, i):
        return i * 2 + 2

    # 注意计算公式
    def getPar(self, i):
        return (i - 1) // 2

    def getLeftVar(self, i):
        return self.getVar(self.getLeft(i))

    def getRightVar(self, i):
        return self.getVar(self.getRight(i))

    def getParVar(self, i):
        return self.getVar(self.getPar(i))

    # 广度优先遍历，即返回数组即可
    def bfs_travel(self):
        for i in range(self.size()):
            if self.__tree[i] is not None:
                self.__res.append(self.getVar(i))


    # 深度优先遍历-前序方式
    # 当元素为None，表明无子节点，回溯返回。这里无须再次判断是否数组越界，因元素为None，就是无子树了，不进行下一步，回溯即可。
    def dfs_pre(self, i):
        if self.getVar(i) is None:
            return
        self.__res.append(self.getVar(i))
        self.dfs_pre(self.getLeft(i))
        self.dfs_pre(self.getRight(i))

    def dfs_mid(self, i):
        if self.getVar(i) is None:
            return
        self.dfs_mid(self.getLeft(i))
        self.__res.append(self.getVar(i))
        self.dfs_mid(self.getRight(i))

    # res定义在构造函数中，如果不清空，多种方法append后，列表内部元素会不断增加
    def clear(self):
        self.__res = []

    def getRes(self):
        return self.__res


if __name__ == "__main__":
    arr = [5, 9, 11, 15, 18, 90, 243, 2, 55]
    print('输入列表为:', arr)
    tree = BinaryTreeList(arr)
    print("第{}个节点元素为{},左节点元素为{},右节点元素为{}".format(3,tree.getVar(3),tree.getLeftVar(3),tree.getRightVar(3)))
    tree.bfs_travel()
    print('广度优先遍历：', tree.getRes())
    tree.clear()
    tree.dfs_pre(0)
    print('深度优先遍历-前序：', tree.getRes())
    tree.clear()
    tree.dfs_mid(0)
    print('深度优先遍历-中序：', tree.getRes())

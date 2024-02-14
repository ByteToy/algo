# 自定义堆的实现，大顶堆
class MaxHeap:
    def __init__(self, nums):
        self.max_heap = []
        #自顶向下建堆，逐个元素压入堆
        for i in nums:
            self.push(i)


    def getVal(self, i):
        # 这里需要判断是否越界，否则深度优先遍历会报错
        if i < 0 or i >= self.size():
            return None
        return self.max_heap[i]

    def getLeft(self, i):
        return i * 2 + 1

    def getRight(self, i):
        return i * 2 + 2

    def getPar(self, i):
        return (i - 1) // 2

    def size(self):
        return len(self.max_heap)

    def isEmpty(self):
        return self.size() == 0

    def dfs_mid(self):
        self.__res=[]
        self.dfs(0,'mid')
        return self.__res

    # 深度优先遍历
    def dfs(self,i,order):
        if self.getVal(i) is None:
            return
        if order=='pre':
            self.__res.append(self.getVal(i))
        self.dfs(self.getLeft(i),order)
        if order=='mid':
            self.__res.append(self.getVal(i))
        self.dfs(self.getRight(i),order)
        if order=='post':
            self.__res.append(self.getVal(i))

    # 交换堆内的两个节点内容
    # python独特的变量互换写法
    def swap(self, i, j):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def peek(self):
        return self.max_heap[0]

    # 新元素入堆
    def push(self, value):
        # 将新元素添加至尾部
        self.max_heap.append(value)
        # 向上移动末尾节点
        self.shift_up(self.size() - 1)

    # 新元素入堆后，需要向上移动至合适位置
    def shift_up(self, i):
        while True:
            # 获取父节点
            p = self.getPar(i)
            # 终止循环条件：达到根节点或者子节点小于根节点
            if p < 0 or self.getVal(i) <= self.getVal(p):
                break
            # 向上移动：交换节点和根节点
            self.swap(i, p)
            # 进入下一步循环：进入父节点
            i = p

    # 堆顶元素出堆
    def pop(self):
        if self.isEmpty():
            raise IndexError("空堆")
        # 堆顶元素与尾部元素互换
        self.swap(0, self.size() - 1)
        # 弹出堆顶元素，此时堆顶元素在最尾部，pop即可
        value = self.max_heap.pop()
        # 堆顶新元素向下移动
        self.shift_down(0)
        return value

    # 堆顶元素向下移动
    def shift_down(self, i):
        while True:
            # 定义三个变量，当前元素、左节点、右节点的数组下标，默认最大值的下标为当前元素
            l, r, mx = self.getLeft(i), self.getRight(i), i
            # 找到三个变量中最大的元素
            # 如果左节点大于最大元素，将mx为左节点
            if l < self.size() and self.max_heap[mx] < self.max_heap[l]:
                mx = l
            # 如果右节点大于最大元素，将mx为右节点
            if r < self.size() and self.max_heap[mx] < self.max_heap[r]:
                mx = r
            # 跳出循环条件：数组遍历结束或当前节点比左右节点都大（此时mx仍然指向i，无须向下遍历）
            if mx == i:
                break
            # 将当前节点与左右节点互换
            self.swap(i, mx)
            # 继续循环条件：进入互换后的下一个节点
            i = mx


if __name__ == "__main__":
    # arr本身就是一个堆，直接传入参数
    # arr = [87, 35, 78, 19, 28, 25, 67, 17, 11]
    arr=[11,17,25,28,19,78,67,87]
    print("输入元素：", arr)
    max_heap = MaxHeap(arr)
    print("查看堆内容：",max_heap.max_heap)
    print("深度优先-中序：",max_heap.dfs_mid())
    # max_heap.push(55)
    # print("入堆后：",max_heap.max_heap)
    val = max_heap.pop()
    print("出堆后：", max_heap.max_heap, val)

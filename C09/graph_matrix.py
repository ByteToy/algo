from prettytable import PrettyTable


class GraphMatrix:
    def __init__(self, verts, edges):
        # 顶点是一个列表
        self.verts = []
        # 边是一个二维列表，是根据顶点N×N的二维列表（数组）
        self.mats = []
        for v in verts:
            self.add_vert(v)

        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self):
        return len(self.verts)

    # 添加顶点
    def add_vert(self, val):
        #
        n = self.size()
        # 顶点列表添加新元素
        self.verts.append(val)
        row = [0] * n
        # 边列表添加一行
        self.mats.append(row)
        # 边列表添加一列（每一行增加一个元素）
        for row in self.mats:
            row.append(0)

    # 删除顶点,根据顶点的索引删除
    def remove_vert(self, i):
        if self.size() == 0:
            raise IndexError("矩阵为空")
        # 顶点列表移除指定索引顶点
        self.verts.pop(i)
        # 边列表移除指定索引顶点行
        self.mats.pop(i)
        # 按行遍历边列表，逐行删除指定索引所在的列
        for row in self.mats:
            row.pop(i)

    # c:行索引，r：列索引
    def add_edge(self, r, c):
        if r < 0 or c < 0 or r >= self.size() or c >= self.size() or r == c:
            raise IndexError('越界')
        self.mats[r][c] = 1
        self.mats[c][r] = 1

    def remove_edge(self, r, c):
        if r < 0 or c < 0 or r >= self.size() or c >= self.size() or r == c:
            raise IndexError('越界')
        self.mats[r][c] = 0
        self.mats[c][r] = 0

    def show(self):
        tb = PrettyTable(self.verts)
        for c in self.mats:
            tb.add_row(c)
        print(tb)


if __name__ == "__main__":
    verts = ['a', 'b', 'c', 'd', 'e']
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    matrix = GraphMatrix(verts, edges)
    matrix.show()

    matrix.add_vert('f')
    matrix.add_edge(1, 5)
    matrix.show()

    matrix.remove_vert(4)
    matrix.show()

    matrix.remove_edge(0, 3)
    matrix.show()

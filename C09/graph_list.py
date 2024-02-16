class GraphList:
    # 基于字典实现无向图的邻接链表
    # 字典的健：顶点(str类型)
    # 字典的值：是一个列表，存储顶点所链接的边list[str]类型
    # edges: list[list[str]]：edges是一个列表，包含多条边，每条边list[str]也是一个列表，包含两个顶点
    def __init__(self, verts: str, edges: list[list[str]]):
        # 初始化一个字典，健为顶点，值为边（list）
        self.graph_list = dict[str, list[str]]()

        # 添加顶点，向字典中添加健
        for v in verts:
            self.add_vert(v)
        # 添加边，向字典中添加健的值
        for e in edges:
            self.add_edge(e[0], e[1])

    # 图的大小，就是顶点个数，即字典的长度
    def size(self):
        return len(self.graph_list)

    # 添加顶点：向字典添加健
    def add_vert(self, v):
        if v in self.graph_list:
            return
        # 仅添加顶点的健，暂无键值
        self.graph_list[v] = []

    # 删除顶点，删除顶点的键值对，同时删除其他顶点内包含该顶点值中包含的顶点
    def remove_vert(self, v):
        if v not in self.graph_list:
            raise ValueError("查无此顶点")
        # 首先删除字典中v健的键值对
        self.graph_list.pop(v)
        # 遍历顶点和链表字典，逐个从字典中顶点对应的键值中，删除v顶点的边
        for vert in self.graph_list:
            if v in vert:
                self.graph_list[vert].remove(v)

    # 增加边：同时修改两个顶点对应的键值
    def add_edge(self, vert1, vert2):
        if vert1 not in self.graph_list or vert2 not in self.graph_list or vert1 == vert2:
            raise ValueError('顶点不存在')
        self.graph_list[vert1].append(vert2)
        # 对键值做个排序，看起来舒服些
        self.graph_list[vert1].sort()
        self.graph_list[vert2].append(vert1)
        self.graph_list[vert2].sort()

    # 删除边：同时删除两个顶点对应的键值
    def remove_edge(self, vert1, vert2):
        if vert1 not in self.graph_list or vert2 not in self.graph_list or vert1 == vert2:
            raise ValueError('顶点不存在')
        self.graph_list[vert1].remove(vert2)
        self.graph_list[vert2].remove(vert1)


if __name__ == "__main__":
    verts = ['a', 'b', 'c', 'd', 'e']
    # edges = [
    #     [verts[0], verts[1]],
    #     [verts[0], verts[3]],
    #     [verts[1], verts[2]],
    #     [verts[2], verts[3]],
    #     [verts[2], verts[4]],
    #     [verts[3], verts[4]],
    #     ]
    edges = [['a', 'b'], ['a', 'd'], ['b', 'c'], ['c', 'd'], ['c', 'e'], ['d', 'e'], ]
    grap_list = GraphList(verts, edges)
    print("大小：",grap_list.size())
    print(grap_list.graph_list)

    grap_list.add_vert('f')
    grap_list.add_edge('b','f')
    print("大小：", grap_list.size())
    print(grap_list.graph_list)

    grap_list.remove_edge('d','e')
    print("大小：", grap_list.size())
    print(grap_list.graph_list)

    grap_list.remove_vert('c')
    print("大小：", grap_list.size())
    print(grap_list.graph_list)


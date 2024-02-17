# 无向图遍历
from collections import deque
from graph_list import GraphList


# 广度优先遍历，通过队列方式实现
def bfs(graph: GraphList, start_vert: str):
    res = []
    # 集合和队列存储顶点，均为str类型，做个注解
    visited = set[str]([start_vert])
    que = deque[str]([start_vert])
    # 获取顶点的邻接顶点，如果没有被访问，就添加至队列中，直到队列元素全部被访问完毕
    # 前提条件是所有节点之间有相连的边，如果有未连接的节点，则无法遍历。
    while len(que) > 0:
        vert = que.popleft()
        res.append(vert)
        # graph_list就是存储图的字典，根据健获取键值，键值是一个列表
        for sub_vert in graph.graph_list[vert]:
            # 如果该顶点已经放问过，则继续循环不甜加至队列
            if sub_vert in visited:
                continue
            que.append(sub_vert)
            visited.add(sub_vert)
    return res


# 深度优先遍历，使用递归方式实现
# 为列便于理解，为变量加上注解
# graph：邻接表实现的无向图
# visited：访问过顶点的集合
# res：访问的节点，这里要与visited区分，他们顺序不同的。这里注意set的属性，有兴趣可以观察set的内容和顺序
def dfs(graph: GraphList, visited: set[str], res: list[str], start_v):
    visited.add(start_v)
    # 经过节点即记录，前序方式
    res.append(start_v)
    # 递归边界条件（终止条件），这里是一种隐性的写法，for循环终止列，即退回到上一步
    for v in graph.graph_list[start_v]:
        if v in visited:
            continue
        # 对连接的新顶点继续遍历
        dfs(graph, visited, res, v)


if __name__ == "__main__":
    verts = ['a', 'b', 'c', 'd', 'e']
    edges = [['a', 'b'], ['a', 'd'], ['b', 'c'], ['c', 'd'], ['c', 'e'], ['d', 'e'], ]
    graph = GraphList(verts, edges)
    print(graph.graph_list)

    print(bfs(graph, 'a'))

    dfs_res = []
    visited = set[str]()
    dfs(graph, visited, dfs_res, 'a')
    print(dfs_res,visited)

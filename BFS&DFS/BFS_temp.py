BTree = {
    10: [5, 15],
    5: [3, 6],
    3: [1, 4],
    15: [12, 16],
    12: [11, 13]
}


def DFS(BTree, start,visited=None):
    if start not in BTree:
        print(start)
        visited.add(start)
        return

    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in BTree[start]:
        if i in visited:
            continue
        DFS(BTree, i,visited)
    return visited


# def BFS(BTree, start):
#     visited = set()
#     queue = []
#     visited.add(start)
#     queue.append(start)
#     while queue:
#         root_node = queue.pop(0)
#         print(root_node)
#         if root_node in BTree:
#             sub_nodes = BTree[root_node]
#             for sub_node in sub_nodes:
#                 if sub_node not in visited:
#                     visited.add(sub_node)
#                     queue.append(sub_node)

DFS(BTree, 10)

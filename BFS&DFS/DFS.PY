BTree = {
    10: [5, 15],
    5: [3, 6],
    3: [1, 4],
    15: [12, 16],
    12: [11, 13]
}


def BFS(graph, start):
    stack = []
    visited = set()
    stack.append(start)
    visited.add(start)
    while stack:
        root_node = stack.pop()
        print(root_node)
        if root_node in graph:
            sub_nodes = graph[root_node]
            for sub_node in sub_nodes:
                if sub_node not in visited:
                    stack.append(sub_node)
                    visited.add(sub_node)
        else:
            continue


BFS(BTree, 5)

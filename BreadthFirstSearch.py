def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vert = queue.pop(0)
        if vert not in visited:
            visited.append(str(vert))
            queue.extend(i for i in graph[str(vert)] if i not in visited)
    return visited

if __name__ == '__main__':
    graph = {'1': ['2', '3'],
         '2': ['1', '3', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}

    print (bfs(graph,1))

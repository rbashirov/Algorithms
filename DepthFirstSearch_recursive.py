def dfs_recurive(graph, start, visited = []):
    visited += str(start)

    for vert in graph[str(start)]:
        if vert not in visited:
            visited = dfs_recurive(graph, vert, visited)
    return visited

if __name__ == '__main__':
    graph = {'1': ['2', '3'],
         '2': ['1', '3', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}

    print (dfs_recurive(graph,1))

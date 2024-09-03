def topologicalSort(edge, v, e):
    
    adj = defaultdict(list)

    for src, dest in edge:
        adj[src].append(dest)
    
    path = []
    vis = set()

    def dfs(src):
        vis.add(src)

        for nei in adj[src]:
            if nei not in vis:
                dfs(nei)
        
        path.append(src)
    
    for i in range(v):
        if i not in vis:
            dfs(i)

    return path[::-1]

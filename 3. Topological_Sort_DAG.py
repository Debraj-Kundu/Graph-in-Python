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

    def bfs(src):
        indegree = [0] * v
        q = deque()
        
        #count indegree
        for val in adj.values():
            for node in val:
                indegree[node] += 1
    
        #push all 0 indegree node in queue
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)
        
        #apply bfs
        while q:
            node = q.popleft()
            path.append(node)
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

    
    for i in range(v):
        if i not in vis:
            dfs(i)
    return path[::-1]
    #-----------------
    bfs(0)
    return path

from collections import defaultdict

def detectCycleInDirectedGraph(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    
    vis = set()
    dfsVis = set()

    def dfs(src):
        vis.add(src)
        dfsVis.add(src)

        for nei in adj[src]:
            if nei not in vis:
                if dfs(nei):
                    return True
            elif nei in dfsVis:
                return True
            
        dfsVis.remove(src)

        return False

    for i in range(1, n+1):
        if i not in vis:
            if dfs(i):
                return True

    return False

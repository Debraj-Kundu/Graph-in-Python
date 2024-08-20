from collections import defaultdict
from collections import deque

def cycleDetection(edges, n, m):

    adj = defaultdict(list)
    vis = set()

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def dfs(src, parent):
        vis.add(src)

        for n in adj[src]:
            if n not in vis:
                if dfs(n, src):
                    return True
            elif n != parent:   
                return True
        
        return False

    def bfs(src):
        parent = {}
        parent[src] = -1
        vis.add(src)
        q = deque()
        q.append(src)

        while q:
            frnt = q.popleft()

            for n in adj[frnt]:
                if n in vis and n != parent[frnt]:  
                    return True
                elif n not in vis:
                    q.append(n)
                    vis.add(n)
                    parent[n] = frnt
            
        return False

    for i in range(n):
        if i not in vis:
            # if dfs(i, -1):
            #     return "Yes"
            if bfs(i):
                return "Yes"
    
    return "No"

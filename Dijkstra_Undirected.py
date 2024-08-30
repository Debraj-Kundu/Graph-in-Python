def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
    
    minHeap = [(0, S)]
    res = [float('inf')] * len(adj)
    vis = set()
    
    while minHeap:
        wt, node = heapq.heappop(minHeap)
        res[node] = min(wt, res[node])
        
        if node not in vis:
            vis.add(node)
            
            for nei, neiWt in adj[node]:
                if nei not in vis:
                    heapq.heappush(minHeap, (wt+neiWt, nei))
    
    return res

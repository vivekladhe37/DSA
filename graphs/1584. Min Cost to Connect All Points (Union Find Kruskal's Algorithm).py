class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(node) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(u,v) -> bool:
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            
            return True
        
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                edges.append((dist, i, j))
        
        edges.sort()

        mst_cost = 0
        edges_used = 0

        for dist, u, v in edges:
            if union(u,v):
                mst_cost += dist
                edges_used += 1
                if edges_used == n-1:
                    break
        
        return mst_cost
    


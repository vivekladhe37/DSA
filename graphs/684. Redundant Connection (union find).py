class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        rank = [1] * (n+1)
        parent = [i for i in range(n+1)]
        res = []

        def find(node) -> int:
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res

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

        for u,v in edges:
            if not union(u,v):
                res.append([u,v])

        return res[-1]
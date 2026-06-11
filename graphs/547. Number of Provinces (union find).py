class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n
        result = n

        def find(city) -> int:
            res = city

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

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1 and union(i,j):
                    result -= 1
        
        return result
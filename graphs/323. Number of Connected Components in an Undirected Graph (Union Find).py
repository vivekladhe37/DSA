# -------------------------------
# Problem: Number of Connected Components (LC 323)
# -------------------------------
# You are given:
#   - an integer n representing nodes labeled 0 to n - 1
#   - a list of undirected edges, where each edge is [u, v]
#
# A connected component is a group of nodes where each node
# is reachable from every other node in that group.
#
# Return the number of connected components in the graph.
# -------------------------------

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        rank = [1] * n
        parent = [i for i in range(n)]
        res = n
        
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
            if union(u,v):
                res -= 1
            
        return res
        


# -------------------------------
# Testcases (Playground Ready)
# -------------------------------

sol = Solution()

tests = [
    {
        "n": 5,
        "edges": [[0,1],[1,2],[3,4]],
        "expected": 2
    },
    {
        "n": 4,
        "edges": [[0,1],[2,3],[1,2]],
        "expected": 1
    },
    {
        "n": 4,
        "edges": [],
        "expected": 4
    },
    {
        "n": 1,
        "edges": [],
        "expected": 1
    },
    {
        "n": 6,
        "edges": [[0,1],[2,3],[4,5]],
        "expected": 3
    },
]

for i, t in enumerate(tests, 1):
    print(f"Test {i}: ", sol.countComponents(t["n"], t["edges"]), " | Expected:", t["expected"])

# -------------------------------
# Problem: Graph Valid Tree (LC 261)
# -------------------------------
# You are given:
#   - an integer n representing nodes labeled 0 to n - 1
#   - a list of undirected edges, where each edge is [u, v]
#
# A graph is a valid tree if:
#   1. It is connected (all nodes reachable)
#   2. It has no cycles
#
# Return True if the graph is a valid tree, otherwise False.
# -------------------------------

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        connectedCheck = n
        
        rank = [1] * n
        parent = [i for i in range(n)]
        
        
        def find(node) -> int:
            res = node
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(u, v) -> bool:
            p1, p2 = find(u), find(v)
            
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            
            return True
  
        for u,v in edges:
            if union(u,v):
                connectedCheck -= 1
            else:
                return False
        
        return connectedCheck == 1
            
            


# -------------------------------
# Testcases (Playground Ready)
# -------------------------------

sol = Solution()

tests = [
    {
        "n": 5,
        "edges": [[0,1],[0,2],[0,3],[1,4]],
        "expected": True
    },
    {
        "n": 5,
        "edges": [[0,1],[1,2],[2,3],[1,3],[1,4]],
        "expected": False
    },
    {
        "n": 4,
        "edges": [[0,1],[2,3]],
        "expected": False
    },
    {
        "n": 1,
        "edges": [],
        "expected": True
    },
    {
        "n": 2,
        "edges": [[0,1]],
        "expected": True
    },
]

for i, t in enumerate(tests, 1):
    print(f"Test {i}: ", sol.validTree(t["n"], t["edges"]), " | Expected:", t["expected"])

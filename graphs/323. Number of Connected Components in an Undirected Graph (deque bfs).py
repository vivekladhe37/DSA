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
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        
        def bfs(q):
            while q:
                node = q.popleft()
                
                seen.add(node)
                
                for nei in graph[node]:
                    if nei not in seen:
                        q.append(nei)
                        
        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                bfs(deque([i]))
        
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

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        
        state = [UNVISITED] * n
        res = []
        
        def dfs(node) -> bool:
            if state[node] == VISITING:
                return False
            if state[node] == VISITED:
                return True
            
            state[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
                    
            state[node] = VISITED
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)
                
        return res
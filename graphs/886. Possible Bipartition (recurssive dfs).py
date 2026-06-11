from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        UNCOLORED = 0
        COLORA = 1
        COLORB = -1
        
        color = [UNCOLORED] * (n + 1)
        graph = defaultdict(list)
        
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(person, c) -> bool:
            color[person] = c
            for nei in graph[person]:
                if color[nei] == color[person]:
                    return False
                elif color[nei] == UNCOLORED:
                    if not dfs(nei, -c):
                        return False
            return True

        for person in range(1, n + 1):
            if color[person] == UNCOLORED:
                if not dfs(person, COLORA):
                    return False

        return True
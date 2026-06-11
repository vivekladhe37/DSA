from typing import List
from collections import defaultdict, deque

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
            
        def bfs(person) -> bool:
            q = deque([person])
            color[person] = COLORA
            
            while q:
                p = q.popleft()
                for nei in graph[p]:
                    if color[nei] == color[p]:
                        return False
                    elif color[nei] == UNCOLORED:
                        q.append(nei)
                        color[nei] = -color[p]
            return True

        for person in range(1, n + 1):
            if color[person] == UNCOLORED:
                if not bfs(person):
                    return False

        return True
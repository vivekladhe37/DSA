class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED = 0
        COLORA = 1
        color = [UNCOLORED] * n

        def dfs(node, c) -> bool:

            color[node] = c

            for nei in graph[node]:
                if color[nei] == color[node]:
                    return False
                elif color[nei] == UNCOLORED:
                    if not dfs(nei, -color[node]):
                        return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i,COLORA):
                    return False
        
        return True
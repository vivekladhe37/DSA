class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = defaultdict(list)
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([source])
        visited.add(source)

        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        if destination not in visited:
            return False
        else:
            return True
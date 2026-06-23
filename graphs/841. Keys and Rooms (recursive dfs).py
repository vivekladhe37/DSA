class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(node):
            for nei in rooms[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        visited.add(0)
        dfs(0)

        return True if len(visited) == n else False
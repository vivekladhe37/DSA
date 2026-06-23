class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        n = len(grid)

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        q = deque([(0,0,1)])
        visited = set([(0,0)])

        while q:

            r, c, dist = q.popleft()

            if (r,c) == (n-1, n-1):
                return dist
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                    q.append((nr,nc,dist + 1))
                    visited.add((nr, nc))

        return -1
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)

        pq = [(grid[0][0], 0,0)]

        visited = [[False for i in range(n)] for j in range(n)]
        visited[0][0] = True

        while pq:

            ele, r, c = heapq.heappop(pq)

            if (r, c) == (n-1, n-1):
                return ele

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    newele = max(ele, grid[nr][nc])
                    heapq.heappush(pq, (newele, nr, nc))
                    visited[nr][nc] = True
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(x, y, c) -> int:

            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or (x, y) in seen:
                return c

            seen.add((x, y))
            c += 1

            for dr, dc in dirs:
                c = dfs(x + dr, y + dc, c)
            
            return c


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    count = dfs(r,c,0)
                    res = max(res, count)

        return res
        
        
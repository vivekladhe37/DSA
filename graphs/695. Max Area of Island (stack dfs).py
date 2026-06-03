class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(s):
            c = 0
            while s:
                x, y = s.pop()
                if (x, y) in seen:
                    continue

                seen.add((x, y))
                c += 1

                for dr, dc in dirs:
                    dx = x + dr
                    dy = y + dc

                    if (
                        0 <= dx < rows and
                        0 <= dy < cols and
                        grid[dx][dy] == 1 and
                        (dx, dy) not in seen
                    ):
                        s.append((dx, dy))

            return c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = dfs([(r, c)])
                    res = max(res, area)

        return res

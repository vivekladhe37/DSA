class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0
        seen = set()
        stack = []

        dirs = [(1,0), (0,-1), (0,1), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(stack):

            while stack:
                x , y = stack.pop()

                for dr, dc in dirs:
                    nr, nc = x + dr, y + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0' or (nr,nc) in seen:
                        continue
                    else:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in seen:
                    stack.append((r,c))
                    seen.add((r, c))
                    dfs(stack)
                    island_count += 1

        return island_count
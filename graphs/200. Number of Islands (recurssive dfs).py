class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0
        seen = set()
        dirs = [(1,0), (0,-1), (0,1), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x,y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == '0' or (x,y) in seen:
                return
            seen.add((x,y))
            for dr, dc in dirs:
                dfs(x + dr, y + dc)


        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c)
                    island_count += 1

        return island_count
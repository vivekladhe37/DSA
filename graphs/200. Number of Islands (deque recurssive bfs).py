class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0
        q = deque()
        seen = set()

        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(q):

            if not q:
                return

            next_level = deque()

            while q:
                x, y = q.popleft()

                for dr, dc in dirs:
                    nx, ny = x + dr, y + dc

                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols and grid[nx][ny] == '1' and(nx, ny) not in seen:
                        seen.add((nx, ny))
                        next_level.append((nx, ny))
            bfs(next_level)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    seen.add((r,c))
                    bfs(deque([r,c]))
                    island_count += 1
            
        return island_count
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        mins = -1

        while q:
            mins += 1
            for _ in range(len(q)):
                    
                x, y = q.popleft()

                for dr, dc in dirs:
                    nr, nc = x + dr, y + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return mins if fresh == 0 else -1
                
 


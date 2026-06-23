class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        landCells = 0
        q = deque()
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if 0 < i < rows-1 and 0 < j < cols-1:
                        landCells += 1
                    else:
                        q.append((i,j))
                        visited.add((i,j))
        
        if not q:
            return landCells

        while q:

            r,c = q.popleft()

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    landCells -= 1

        

        return landCells

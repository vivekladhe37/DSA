class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        seenPacific = set()
        seenAtlantic = set()
        res = []

        def dfs_pacific(r, c):
            if (r, c) in seenPacific:
                return
            seenPacific.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs_pacific(nr, nc)

        def dfs_atlantic(r,c):
            if (r, c) in seenAtlantic:
                return
            seenAtlantic.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs_atlantic(nr, nc)

        for r in range(rows):
            dfs_pacific(r, 0)
        for c in range(cols):
            dfs_pacific(0, c)
        for r in range(rows):
            dfs_atlantic(r, cols-1)
        for c in range(cols):
            dfs_atlantic(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seenAtlantic and (r, c) in seenPacific:
                    res.append([r,c])
        return res



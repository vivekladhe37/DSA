class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        i = sr
        j = sc
        seen = set()
        rows = len(image)
        cols = len(image[0])

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        tar = image[i][j]

        if image[i][j] == color:
            return image

        def dfs(x,y):

            if x < 0 or y < 0 or x >= rows or y >= cols or image[x][y] != tar or (x,y) in seen:
                return

            image[x][y] = color
            seen.add((x,y))
            
            for dr, dc in dirs:
                dfs(x + dr, y + dc)

        dfs(i,j)

        return image
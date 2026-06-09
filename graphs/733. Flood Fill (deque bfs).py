class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        curr_pixel = image[sr][sc]
        seen = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()

        def bfs(x,y):

            while q:
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == curr_pixel and (nr, nc) not in seen:
                        image[nr][nc] = color
                        q.append((nr, nc))
                        seen.add((nr, nc))
                
        image[sr][sc] = color
        q.append((sr,sc))
        seen.add((sr,sc))
        bfs(sr,sc)

        return image
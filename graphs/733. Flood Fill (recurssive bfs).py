class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        curr_pixel = image[sr][sc]
        seen = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque([(sr, sc)])

        def bfs(q):

            if not q:
                return
            
            next_q = deque()

            while q:
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == curr_pixel and (nr, nc) not in seen:
                        image[nr][nc] = color
                        next_q.append((nr, nc))
                        seen.add((nr, nc))
            bfs(next_q)
                
        image[sr][sc] = color
        seen.add((sr,sc))
        bfs(q)

        return image
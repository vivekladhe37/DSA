class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        n = len(points)

        for cords in points:
            x = cords[0]
            y = cords[1]
            dist = x**2 + y**2

            heapq.heappush(heap,(-dist,[x,y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [points for _, points in heap]



        
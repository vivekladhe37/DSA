class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minDist = [float("inf")] * n
        minDist[0] = 0

        minHeap = [(0,0)]
        totalCost = 0

        while minHeap:
            cost, i = heapq.heappop(minHeap)

            if visited[i] == True:
                continue
            
            visited[i] = True
            totalCost += cost

            x1, y1 = points[i]
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    dist = abs(x2 - x1) + abs(y2 - y1)

                    if dist < minDist[j]:
                        minDist[j] = dist
                        heapq.heappush(minHeap, (dist, j))
            
        return totalCost
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for s,d,p in flights:
            graph[s].append((d,p))
        
        best = defaultdict(lambda: defaultdict(lambda: float("inf")))
        best[src][0] = 0
        minHeap = [(0, src, 0)]

        while minHeap:
            price, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return price
            if stops > k:
                continue
            
            for nei,p in graph[node]:
                newPrice = price + p
                if newPrice < best[nei][stops + 1]:
                    best[nei][stops+1] = newPrice
                    heapq.heappush(minHeap, (newPrice, nei, stops+1))
                

        return -1


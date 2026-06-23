class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        nodeTime = [float("inf")] * (n+1)
        nodeTime[k] = 0
        minHeap = []

        for u,v,w in times:
            graph[u].append((v,w))
        
        heapq.heappush(minHeap, (0,k))

        while minHeap:

            time, node = heapq.heappop(minHeap)

            if time > nodeTime[node]:
                continue

            for nei,t in graph[node]:
                neiTime = t + time
                if nodeTime[nei] > neiTime:
                    heapq.heappush(minHeap,(neiTime,nei))
                    nodeTime[nei] = neiTime

        res = max(nodeTime[1:])

        return res if res != float("inf") else -1
                
        
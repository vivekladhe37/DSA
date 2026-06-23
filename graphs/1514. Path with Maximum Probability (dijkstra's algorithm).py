class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)

        for (u,v), p in zip(edges, succProb):
            graph[u].append((v,p))
            graph[v].append((u,p))

        maxHeap = [(-1.0, start_node)]

        best = [0.0] * n
        best[start_node] = 1.0

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob = -prob

            if node == end_node:
                return prob

            for nei, p in graph[node]:
                newprob = p * prob
                if newprob > best[nei]:
                    best[nei] = newprob
                    heapq.heappush(maxHeap, (-newprob, nei))

        return 0.0




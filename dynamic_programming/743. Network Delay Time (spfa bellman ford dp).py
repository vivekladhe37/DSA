class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTime = [float("inf")] * (n + 1)
        minTime[k] = 0
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        q = deque([k])
        
        while q:
            node = q.popleft()
            w = minTime[node]
            for nei, wei in graph[node]:
                newWei = w + wei
                if newWei < minTime[nei]:
                    minTime[nei] = newWei
                    q.append(nei)
                    
        res = max(minTime[1:])
        return res if res != float("inf") else "-1"

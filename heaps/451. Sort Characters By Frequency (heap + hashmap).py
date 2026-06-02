class Solution:
    def frequencySort(self, s: str) -> str:
        maxHeap = []
        fmap = defaultdict(int)
        res = []
        for c in s:
            fmap[c] += 1
        for key, value in fmap.items():
            heapq.heappush(maxHeap, (-value, key))
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            freq = -freq
            res.append(char * freq)
        return "".join(res)
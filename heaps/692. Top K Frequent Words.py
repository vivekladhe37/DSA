class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        fmap = defaultdict(int)
        maxHeap = []
        res = []
        n = len(words)
        

        for word in words:
            fmap[word] += 1

        for word, freq in fmap.items():
            heapq.heappush(maxHeap, (-freq, word))

        while len(res) != k:
            freq, word = heapq.heappop(maxHeap)
            res.append(word)
        


        return res

        
        
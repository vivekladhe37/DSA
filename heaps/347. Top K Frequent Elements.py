class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        fmap = defaultdict(int)
        heap = []

        for num in nums:
            fmap[num] += 1
        
        for num, freq in fmap.items():
            heapq.heappush(heap,(freq, num))
            if len(heap) > k:
                heappop(heap)
        
        return [num for _, num in heap]
            



        
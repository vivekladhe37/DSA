class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = []
        
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            f_stone = -heapq.heappop(maxHeap)
            s_stone = -heapq.heappop(maxHeap)
            diff = abs(f_stone - s_stone)
            if diff != 0:
                heapq.heappush(maxHeap, -diff)
            
        return -maxHeap[0] if maxHeap else 0
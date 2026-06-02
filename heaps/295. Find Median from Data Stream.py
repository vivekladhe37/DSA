class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.minl = 0
        self.maxl = 0

    def addNum(self, num: int) -> None:
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap, -num)
        else:
            if num > -(self.maxheap[0]):
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)

        self.minl , self.maxl = len(self.minheap) , len(self.maxheap)

        if self.minl > self.maxl + 1:
            heapq.heappush(self.maxheap, -(heapq.heappop(self.minheap)))
        elif self.maxl > self.minl + 1:
            heapq.heappush(self.minheap, -(heapq.heappop(self.maxheap)))

        self.minl , self.maxl = len(self.minheap) , len(self.maxheap)

    def findMedian(self) -> float:
        if self.minl == self.maxl:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif self.minl > self.maxl:
            return self.minheap[0]
        else:
            return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
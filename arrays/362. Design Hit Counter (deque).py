class HitCounter:

    def __init__(self):
        self.priority_queue = deque()
        

    def hit(self, timestamp: int) -> None:
        # record a hit at this timestamp
        self.priority_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # return number of hits in [timestamp - 299, timestamp]
        while self.priority_queue and self.priority_queue[0] < (timestamp - 300):
            self.priority_queue.popleft()

        return len(self.priority_queue)
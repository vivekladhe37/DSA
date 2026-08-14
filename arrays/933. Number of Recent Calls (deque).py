class RecentCounter:

    def __init__(self):
         self.priority_queue = deque()
        

    def ping(self, t: int) -> int:
        self.priority_queue.append(t)

        while self.priority_queue[0] < (t - 3000):
            self.priority_queue.popleft()

        return len(self.priority_queue)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
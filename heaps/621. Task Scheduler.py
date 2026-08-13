class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq_dictionary = defaultdict(int)

        for task in tasks:
            freq_dictionary[task] += 1
        
        maxHeap = [(-freq, task) for task, freq in freq_dictionary.items()]
        heapq.heapify(maxHeap)
        time = 0


        while maxHeap:
            temp = []
            scheduled = 0

            for i in range(n+1):
                if maxHeap:
                    freq, task = heapq.heappop(maxHeap)
                    scheduled += 1
                    freq = -freq
                    freq -= 1
                    if freq > 0:
                        temp.append((-freq, task))
                
            for item in temp:
                heapq.heappush(maxHeap, item)
                    
            time += (n + 1) if maxHeap else scheduled

        return time
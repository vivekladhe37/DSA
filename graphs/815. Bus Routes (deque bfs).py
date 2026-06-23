class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        graph = defaultdict(list)
        numBuses = len(routes)

        for i in range(numBuses):
            for stop in routes[i]:
                graph[stop].append(i)
        
        q = deque([source])
        visited_stops = set([source])
        visited_buses = set()
        buses_taken = 0

        while q:
            buses_taken += 1

            for _ in range(len(q)):
                s = q.popleft()

                for bus in graph[s]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)

                    for stop in routes[bus]:
                        if stop == target:
                            return buses_taken
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            q.append(stop)

        return -1
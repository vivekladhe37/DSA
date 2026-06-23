class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)

        route = []
        stack = ["JFK"]

        while stack:

            top = stack[-1]

            if graph[top]:
                next_airport = graph[top].pop()
                stack.append(next_airport)
            else:
                route.append(stack.pop())

        return route[::-1]
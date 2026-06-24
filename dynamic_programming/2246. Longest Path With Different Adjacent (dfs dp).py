class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph = defaultdict(list)
        n = len(parent)

        for i in range(1,n):
            graph[parent[i]].append(i)

        self.res = 1

        def dfs(node):
            longest = 0
            second_longest = 0

            for nei in graph[node]:
                child_len = dfs(nei)

                if s[nei] == s[node]:
                    continue
                
                if child_len > longest:
                    second_longest = longest
                    longest = child_len
                else:
                    second_longest = max(child_len, second_longest)
                
                self.res = max(self.res, 1 + longest + second_longest)
            
            return longest + 1


        dfs(0)

        return self.res
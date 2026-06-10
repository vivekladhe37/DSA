from typing import List
from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        nodeDict = defaultdict(list)
        
        for node1, node2 in edges:
            nodeDict[node1].append(node2)
            nodeDict[node2].append(node1)
            
        visited = set()
        
        def bfs(q):
            while q:
                node, parent = q.popleft()
                
                visited.add(node)
                
                for nei in nodeDict[node]:
                    if nei == parent:
                        continue
                    elif nei in visited:
                        return False
                    else:
                        q.append((nei, node))
                        
            return True
            
        q = deque()
        q.append((0,-1))
        
        if not bfs(q):
            return False
        
        return len(visited) == n

# ✅ Test cases
def run_tests():
    sol = Solution()

    test_cases = [
        # (n, edges, expected_output)
        (5, [[0,1],[0,2],[0,3],[1,4]], True),
        (5, [[0,1],[1,2],[2,3],[1,3],[1,4]], False),
        (4, [[0,1],[2,3]], False),
        (1, [], True),
        (2, [[0,1]], True),
        (3, [[0,1],[1,2],[0,2]], False),
    ]

    for i, (n, edges, expected) in enumerate(test_cases):
        result = sol.validTree(n, edges)
        print(f"Test Case {i+1}: ", end="")

        if result == expected:
            print("✅ Passed")
        else:
            print("❌ Failed")
            print(f"   Input: n={n}, edges={edges}")
            print(f"   Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        original_to_new = {}

        def dfs(original):

            if original in original_to_new:
                return original_to_new[original]
            
            copy = Node(original.val)
            original_to_new[original] = copy

            for nei in original.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)



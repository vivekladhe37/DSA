# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            longest = 0
            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            if left_len > right_len:
                longest = left_len
            else:
                longest = right_len

            return 1 + longest

        res = dfs(root)
        return res




        
        
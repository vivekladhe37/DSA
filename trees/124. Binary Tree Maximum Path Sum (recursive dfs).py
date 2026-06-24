# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ressum = float("-inf")

        def dfs(node):
            
            if not node:
                return 0

            left_child_sum = max(0, dfs(node.left))
            right_child_sum = max(0, dfs(node.right))

            self.ressum = max(self.ressum, right_child_sum + left_child_sum + node.val)

            return node.val + max(right_child_sum, left_child_sum)
            

        dfs(root)

        return self.ressum
        
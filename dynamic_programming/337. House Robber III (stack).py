# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue
            
            if not visited:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                left_rob, left_not = dp.get(node.left, (0,0))
                right_rob, right_not = dp.get(node.right, (0,0))

                rob = node.val + left_not + right_not
                not_rob = max(left_rob, left_not) + max(right_rob, right_not)

                dp[node] = (rob, not_rob)

        return max(dp[root])
            

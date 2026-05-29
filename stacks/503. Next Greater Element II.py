class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        
        stack = []
        n = len(nums)
        res = [-1] * n
        i = 0
        

        for idx in range(2 * n):
            i = idx % n
            while stack and nums[i] > stack[-1][0]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            if idx < n:
                stack.append((nums[i],i))
        
        return res
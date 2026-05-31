class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        l = 0
        stack = []
        resArea = 0

        for r in range(len(heights)):
            l = r
            curheight = heights[r]
            while stack and curheight < stack[-1][0]:
                resArea = max(resArea, stack[-1][0] * (r - stack[-1][1]))
                l = stack[-1][1]
                stack.pop()
                

            

            stack.append((curheight, l))
        while stack:
            height, start = stack.pop()
            resArea = max(resArea, height * (len(heights) - start))

        return resArea
        
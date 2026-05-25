class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        low = 0
        high = n-1
        maxWater = 0

        while low < high:
            breadth = high - low
            length = min(height[low], height[high])
            area = length * breadth

            maxWater = max(maxWater, area)

            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1 

        return maxWater

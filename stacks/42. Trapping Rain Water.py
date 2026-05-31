class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        res = 0

        for r in range(len(height)):
            currentHeight = height[r]

            while stack and currentHeight > stack[-1][0]:
                valley_height, valley_index = stack.pop()

                if not stack:
                    break

                left_height, left_index = stack[-1]

                water_height = min(left_height, currentHeight) - valley_height
                if water_height <= 0:
                    continue

                width = r - left_index - 1

                res += water_height * width

            stack.append((currentHeight, r))

        return res

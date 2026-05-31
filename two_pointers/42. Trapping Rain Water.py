class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        lmaxarr = [0] * n
        rmaxarr = [0] * n
        water = 0

        lmax = 0
        rmax = 0

        for i in range(n):
            lmaxarr[i] = lmax
            lmax = max(lmax, height[i])

            rmaxarr[-i - 1] = rmax
            rmax = max(rmax, height[-i-1])

        for i in range(n):
            potWater = min(lmaxarr[i], rmaxarr[i]) - height[i]
            if potWater > 0:
                water += potWater

        return water
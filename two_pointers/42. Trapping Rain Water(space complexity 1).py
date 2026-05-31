class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        lmax = height[l]
        rmax = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    water += lmax - height[l]
                l+= 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    water += rmax - height[r]
                r-= 1
        return water 

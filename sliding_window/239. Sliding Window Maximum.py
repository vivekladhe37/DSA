class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l, r = 0, 0
        max_arr = []
        current_max = float("-inf")
        n = len(nums)
        window = 0

        for r in range(n):
            
            current_max = max(current_max, nums[r])

            if r - l + 1 == k:
                max_arr.append(current_max)
                l += 1
        
        return max_arr


        
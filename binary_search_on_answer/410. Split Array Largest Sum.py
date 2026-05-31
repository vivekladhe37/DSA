class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can_split(mid : int) -> bool:

            summ = 0
            subarrays = 1

            for num in nums:
                
                if summ + num > mid:
                    subarrays += 1
                    summ = 0
                
                summ += num

            return subarrays <= k


        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (right + left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left


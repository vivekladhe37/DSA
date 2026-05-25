class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = 0
        zeros = 0
        result = 0

        for end, num in enumerate(nums):
            zeros += (1 if num == 0 else 0)

            while zeros > k:
                zeros -= (1 if nums[start] == 0 else 0)
                start += 1

            result = max(result, end - start + 1)
        
        return result
        
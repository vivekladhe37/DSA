class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        l = 0
        lsMax = -1
        lsMin = -1
        validSubs = 0

        for r in range(len(nums)):
            if nums[r] < minK or nums[r] > maxK:
                l = r + 1
                lsMin = -1
                lsMax = -1
                continue

            if nums[r] >= minK and nums[r] <= maxK:
                if nums[r] == maxK:
                    lsMax = r
                if nums[r] == minK:
                    lsMin = r
            
            if lsMin > -1 and lsMax > -1:
                validSubs += min(lsMin, lsMax) - l + 1
            
            

        return validSubs
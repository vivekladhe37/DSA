class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def maxsubarrayshelper(k : int) -> int:
            l = 0
            maxkd = defaultdict(int)
            maxkarrays = 0
            for r in range(len(nums)):
                maxkd[nums[r]] += 1

                if len(maxkd) > k:
                    while len(maxkd) > k:
                        maxkd[nums[l]] -= 1
                        if maxkd[nums[l]] == 0:
                            del maxkd[nums[l]]
                        l += 1
                    
                maxkarrays += r - l + 1
            return maxkarrays
            
        return maxsubarrayshelper(k) - maxsubarrayshelper(k-1)

            

            
            


        
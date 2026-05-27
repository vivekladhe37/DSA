class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        psum = 0
        res = 0
        pdict = defaultdict(int)
        pdict[0] = 1

        for i in range(len(nums)):

            psum += nums[i]

            if nums[i] % k == 0:
                res += pdict[psum % k] - 1
            else:
                res += pdict[psum % k]
            
            if res > 0:
                return True

            pdict[psum%k] += 1

        return False
        
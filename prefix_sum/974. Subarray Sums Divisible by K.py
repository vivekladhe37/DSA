class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        res = 0
        s = 0
        rd = defaultdict(int)
        rd[0] = 1

        for i in range(len(nums)):
            s += nums[i]

            res += rd[s%k]

            rd[s%k] += 1
        
        return res
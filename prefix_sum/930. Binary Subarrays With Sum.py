class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = 0
        res = 0
        pdict = defaultdict(int)

        pdict[0] = 1

        for num in nums:
            s += num

            res += pdict[s - goal]

            pdict[s] += 1

        return res
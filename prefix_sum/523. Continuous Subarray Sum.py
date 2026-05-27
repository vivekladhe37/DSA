class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod_index = {0: -1}   # mod → earliest index
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k

            if mod in prefix_mod_index:
                # ensure subarray length ≥ 2
                if i - prefix_mod_index[mod] >= 2:
                    return True
            else:
                # store earliest index only
                prefix_mod_index[mod] = i

        return False

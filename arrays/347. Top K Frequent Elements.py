class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        res_arr = [[] for _ in range(n+1)]
        freq_dict = defaultdict(int)
        result_arr = []

        for num in nums:
            freq_dict[num] += 1

        for key, value in freq_dict.items():
            res_arr[value].append(key)


        for i in range(n, -1, -1):
            for num in res_arr[i]:
                result_arr.append(num)
                if len(result_arr) == k:
                    return result_arr





        
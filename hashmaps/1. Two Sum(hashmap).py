class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for i in range(len(nums)):
            mydict[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]


            if y in mydict and mydict[y] != i:
                return [i, mydict[y]]
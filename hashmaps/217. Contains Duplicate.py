class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        mydict = defaultdict(int)

        for i in range(len(nums)):
            mydict[nums[i]] += 1
            if mydict[nums[i]] == 2:
                return True
        
        return False
    
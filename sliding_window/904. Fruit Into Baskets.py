class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        checkdict = dict()
        start = 0
        res = 0

        for end, ftype in enumerate(fruits):
            checkdict[ftype] = 1 + checkdict.get(ftype, 0)

            while(len(checkdict) > 2):
                checkdict[fruits[start]] -= 1
                if checkdict[fruits[start]] == 0:
                    del checkdict[fruits[start]]
                start += 1

            
            
            res = max(res, end - start + 1)

        return res
        
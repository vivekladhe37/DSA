class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(m: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + m - 1) // m
            return hours <= h
        
        left = 1 
        right = max(piles)

        while left < right:
            mid = (right + left) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left



        
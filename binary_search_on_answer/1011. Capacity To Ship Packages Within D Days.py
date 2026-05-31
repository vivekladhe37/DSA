class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        def can_carry(capacity: int) -> bool:
        
            loadSize = 0
            calDays = 1

            for w in weights:

                loadSize += w

                if loadSize > capacity:
                    calDays += 1
                    loadSize = w

            return calDays <= days 
  

        while left < right:

            mid = (right + left) // 2

            if can_carry(mid):
                right = mid
            else:
                left = mid + 1

                
        return left



        
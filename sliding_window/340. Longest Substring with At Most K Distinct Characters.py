class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        fm = defaultdict(int)
        result = 0
        n = len(s)
        l = 0
        
        for r in range(n):
            char = s[r]
            fm[char] += 1
            
            while len(fm) > k:
                
                fm[s[l]] -= 1
                
                if fm[s[l]] == 0:
                    del fm[s[l]]
                
                l += 1
            
            result = max(result, r - l + 1)
            
        return result

sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))  # Expected 3
print(sol.lengthOfLongestSubstringKDistinct("aa", 1))     # Expected 2

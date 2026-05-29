class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Write your code here
        
        fm = defaultdict(int)
        result = 0
        l = 0
        
        for r in range(len(s)):
            
            char = s[r]
            fm[char] += 1
            
            while len(fm) > 2:
                
                fm[s[l]] -= 1
                
                if fm[s[l]] == 0:
                    del fm[s[l]]
        
                l+= 1
        
            result = max(result, r - l + 1)
                
        return result
                

# Test cases
sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))  # Expected 3
print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # Expected 5

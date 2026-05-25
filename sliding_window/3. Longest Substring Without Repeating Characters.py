class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cdict = dict()
        count = 0
        n = len(s)
        l,r = 0,0

        while r != n:
            if s[r] in cdict:
                l = max(l, cdict[s[r]] + 1)
                
            cdict[s[r]] = r
            count = max(count, r-l+1)
            r += 1
        
        return count


        
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        tdict = {}
        sdict = {}

        res, reslen = [-1, -1], float("inf")

        for i in range(len(t)):
            tdict[t[i]] = 1 + tdict.get(t[i], 0)
        
        have, need = 0, len(tdict)

        l = 0

        for r in range(len(s)):
            c = s[r]
            sdict[c] = 1 + sdict.get(c, 0)
            if c in tdict and sdict[c] == tdict[c]:
                have+= 1
            while(have == need):
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                sdict[s[l]] -= 1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""


        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        if slen != tlen:
            return False
        else:
            for i in range(len(s)):
                sdict[s[i]] += 1
                tdict[t[i]] += 1
            return sdict == tdict 
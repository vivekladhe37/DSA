class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        slen = len(s)
        plen = len(p)

        if plen > slen:
            return []

        result = []

        pcount = [0] * 26
        scount = [0] * 26

        for i in range(plen):
            pcount[ord(p[i]) - 97] += 1
            scount[ord(s[i]) - 97] += 1

        if pcount == scount:
            result.append(0)
        
        for i in range(plen, slen):
            scount[ord(s[i]) - 97] += 1
            scount[ord(s[i - plen]) - 97] -= 1

            if pcount == scount:
                result.append(i-plen+1)
        
        return result

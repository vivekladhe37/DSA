class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for word in strs:
            myarr = [0]*26
            for letter in word:
                myarr[ord(letter)-ord('a')] += 1
            mydict[tuple(myarr)].append(word)
        
        return list(mydict.values())

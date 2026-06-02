class Solution:
    def frequencySort(self, s: str) -> str:
        fmap = defaultdict(int)
        resBucket = [[] for _ in range(len(s) + 1)]
        res = []

        for c in s:
            fmap[c] += 1

        for char, freq in fmap.items():
            resBucket[freq].append(char)

        for i in range(len(s), 0, -1):
            for char in resBucket[i]:
                res.append(char * i)

        return "".join(res)

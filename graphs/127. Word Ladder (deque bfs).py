class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        L = len(wordList[0])

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set(beginWord)

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for nei in patterns[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level+1))

                patterns[pattern] = []             
            
        return 0



        
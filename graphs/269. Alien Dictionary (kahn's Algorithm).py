class Solution:
    def alienOrder(self, words):
       
        adj = {c: set() for w in words for c in w}
        inDegree = {c: 0 for w in words for c in w}
       
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
           
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
           
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break
       
        q = deque([c for c in inDegree if inDegree[c] == 0])
        res = []
       
        while q:      
            c = q.popleft()
            res.append(c)
           
            for nei in adj[c]:
                inDegree[nei] -= 1  
                if inDegree[nei] == 0:
                    q.append(nei)
                   
        return "".join(res) if len(res) == len(inDegree) else ""
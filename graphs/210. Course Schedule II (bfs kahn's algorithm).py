class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        inDegree = [0] * numCourses
        courseDict = defaultdict(list)
        res = []

        for course, pre in prerequisites:
            courseDict[pre].append(course)
            inDegree[course] += 1

        q = deque([i for i in range(numCourses) if inDegree[i] == 0])
        processed = 0

        while q:
            course = q.popleft()
            res.append(course)
            processed += 1
            
            for nxt in courseDict[course]:
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)
        
        return res if processed == numCourses else []
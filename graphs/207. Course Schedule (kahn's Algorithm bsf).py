class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseDict = defaultdict(list)
        inDegree = [0] * numCourses

        for course, pre in prerequisites:
            courseDict[pre].append(course)
            inDegree[course] += 1
        
        q = deque([i for i in range(numCourses) if inDegree[i] == 0])
        processed = 0

        while q:

            course = q.popleft()
            processed += 1

            for nei in courseDict[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)

        return processed == numCourses
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        res = []

        status = [UNVISITED] * numCourses

        courseDict = defaultdict(list)

        for course, pre in prerequisites:
            courseDict[course].append(pre)

        def dfs(course) -> bool:

            if status[course] == VISITED:
                return True
            elif status[course] == VISITING:
                return False
            
            status[course] = VISITING

            for nei in courseDict[course]:
                if not dfs(nei):
                    return False
            
            status[course] = VISITED
            res.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
      
        return res
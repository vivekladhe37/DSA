class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseDict = defaultdict(list)

        for pre in prerequisites:
            courseDict[pre[0]].append(pre[1])

        path = set()
        visited = set()

        def dfs(course) -> bool:
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)

            for pre in courseDict[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            visited.add(course)a
            
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
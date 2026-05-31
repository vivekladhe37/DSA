class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        
        l = 0
        res = 0

        matrix = [[int(x) for x in row] for row in matrix]
        

        for row in range(len(matrix)):
            stack = []
            for r in range(len(matrix[row])):
                l = r
                if row < len(matrix) - 1:
                    if matrix[row+1][r] == 1:
                        matrix[row+1][r] += matrix[row][r]
                
                while stack and matrix[row][r] < stack[-1][0]:
                    res = max(res, stack[-1][0] * (r - stack[-1][1]))
                    l = stack[-1][1]
                    stack.pop()


                stack.append((matrix[row][r],l))
            while stack:
                height, start = stack.pop()
                res = max(res, height * (len(matrix[row]) - start))
        
        return res

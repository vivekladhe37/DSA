class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        indexStack = []
        n = len(temperatures)
        res = [0] * n

        for index, temp in enumerate(temperatures):
            while indexStack and temp > temperatures[indexStack[-1]]:
                res[indexStack[-1]] = index - indexStack[-1]
                indexStack.pop()
            indexStack.append(index)
            
        return res
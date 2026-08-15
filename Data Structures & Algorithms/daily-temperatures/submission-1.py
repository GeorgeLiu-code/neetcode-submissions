class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures=[30,38,30,36,35,40,28]
        # find which have more bigger then clean stack
        
        res = [0] * len(temperatures)
        stack = []
        for i,n in enumerate(temperatures):
            while stack and stack[-1][0] < n :
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((n,i))
        return res

        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftMost = [-1] * n
        for i in range(n):                                    # if heights=[2,2,2]
            while stack and heights[i] <= heights[stack[-1]]: # <= is required
                stack.pop()                                   
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [n] * n
        for j in range(n-1,-1,-1):
            while stack and heights[j] <= heights[stack[-1]]: # <= is required
                stack.pop()
            if stack:
                rightMost[j] = stack[-1]
            stack.append(j)
            
        maxArea = 0
        for k in range(n):
            area = heights[k] * ((rightMost[k]-1)-(leftMost[k]+1)+1)
            maxArea = max(maxArea,area)
        return maxArea
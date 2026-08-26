class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [n] * n
        for j in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                rightMost[j] = stack[-1]
            stack.append(j)
        
        maxArea = 0
        for k in range(n):
            width = (rightMost[k]-1) - (leftMost[k]+1) + 1
            area = width * heights[k]
            maxArea = max(maxArea,area)
        return maxArea

        
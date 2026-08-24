class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)+1):
            while stack and (i == len(heights) or  heights[i] <= heights[stack[-1]]):
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    right = i
                    left = stack[-1]
                    width = right - left - 1 
                area = height * width
                maxArea = max(maxArea,area)
            stack.append(i)
        return maxArea
        
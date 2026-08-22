class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [2,1,5,6]
        stack = []
        maxArea = 0
        for i in range(len(heights)+1):
            while stack and ((i==len(heights)) or (heights[i] <= heights[stack[-1]])):
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1 # think
                area = height * width
                maxArea = max(maxArea,area)
            stack.append(i)
        return maxArea



        
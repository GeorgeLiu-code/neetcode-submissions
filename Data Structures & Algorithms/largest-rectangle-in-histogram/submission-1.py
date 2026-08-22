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
                    width = i - stack[-1] - 1 # right bound - left bound - 1
                area = height * width         # because stack are strictly increase (height or index)
                maxArea = max(maxArea,area)   # so right bound are always bigger than current height[i]. left bound always smaller
            stack.append(i)
        return maxArea



        

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [2,1,5,6]
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index,height = stack.pop()
                start = index # back to last index because h=1 can in index 0
                maxArea = max(maxArea,height * (i - index))
            stack.append((start,h))
        # print(stack)
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea

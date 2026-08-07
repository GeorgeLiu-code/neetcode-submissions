class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = [1,7,2,5,4,7,3,6]
        max_area = 0
        left,right = 0,len(heights)-1
        while left < right:
            min_height = min(heights[left],heights[right])
            width = right - left
            area = min_height * width
            max_area = max(max_area,area)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -= 1
            # if heights[left]>heights[right]:
            #     right -=1
            # else:
            #     left += 1
            
        return max_area




        
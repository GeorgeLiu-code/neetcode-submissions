class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,2,0,3,1,0,1,3,2,1]
        # small height to big is correct 
        # if use big to small will collect more water
        # but can't release this extra water

        left,right = 0,len(height)-1
        res = 0
        leftmax = height[0]
        rightmax = height[len(height)-1]
        while left<right:
            if height[left] < height[right]:
                left += 1
                leftmax = max(leftmax,height[left])
                res += leftmax - height[left]
            else: # when height[right] < height[left]
                right -= 1
                rightmax = max(rightmax,height[right])
                res += rightmax - height[right] 
        return res


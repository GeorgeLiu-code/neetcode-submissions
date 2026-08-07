class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [4,1,2]
        # leftmax[0]=4 leftmax[1]=4 leftmax[2]=4 
        # rightmax[2]=2 rightmax[1]=2 rightmax[0]=4
        # i=0 res = 4-4=0, i=1 res=2-1=1, i=2 res=1+2-2=1
        if not height:
            return 0
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        res = 0
        leftmax[0] = height[0]
        rightmax[n-1] = height[n-1]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1],height[i])
        for j in range(n-2,-1,-1):
            rightmax[j] = max(rightmax[j+1],height[j])
        for k in range(n):
            res += min(leftmax[k],rightmax[k]) - height[k]
        return res

        
class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [4,1,2]
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0]= height[0]
        right[n-1] = height[n-1] 
        res = 0
        for i in range(1,n): 
            left[i] = max(left[i-1],height[i])
        for j in range(n-2,-1,-1):
            right[j] = max(right[j+1],height[j])
        for k in range(n):
            res += min(left[k],right[k])-height[k]
        return res


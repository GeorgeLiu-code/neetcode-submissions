class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [4,1,2,3]
        # stack=[0,1] then i=2 mid=H[1]=1 stack=[0] right=2 left=4
        # h=2-1=1 w=2-0-1=1 res=1 stack=[0,2]
        # i=3 mid=H[2]=2 stack=[0] right=3 left=4 h=3-2=1 w=3-0-1=2
        # res=1+2=3
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[i]>height[stack[-1]]: 
                # like [5,4,3,4] so need use loop
                # pop index 3 then pop index 4
                # buttom up to add water
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    high = min(left,right) - mid
                    width = i - stack[-1] -1
                    res += high * width
            stack.append(i) 
        return res         


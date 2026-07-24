class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # LHS = [1,1,2,8] RHS = [48,24,6,1]
        # LHS * RHS = [48,24,12,8]
        
        res = [1] * len(nums)
        temp = 1
        for i in range(len(nums)): # LHS
            res[i] = temp
            temp = temp * nums[i] 
        
        temp = 1
        for i in range(len(nums)-1, -1, -1): #RHS
            res[i] = res[i] * temp
            temp = temp * nums[i]
        return res

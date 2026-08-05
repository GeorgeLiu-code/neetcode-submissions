class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left,right = i + 1,len(nums)-1
            while left<right:
                target = n+nums[left]+nums[right]
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    ans = [n,nums[left],nums[right]]
                    res.append(ans)
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1] :
                        left += 1
        return res
        
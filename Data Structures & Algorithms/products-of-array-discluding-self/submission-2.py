class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = []
        temp_pre = 1
        for i in range(len(nums)):
            prefix[i] *= temp_pre
            temp_pre *= nums[i]

        temp_suf = 1
        for j in range(len(nums)-1, -1 ,-1):
            suffix[j] *= temp_suf
            temp_suf *= nums[j]

        for i, j in zip(prefix, suffix):
            result.append( i*j )

        return result
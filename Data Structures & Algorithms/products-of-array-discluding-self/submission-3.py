class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        temp = 1
        count_zero = 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                temp *= nums[i]
            else:
                count_zero += 1
        if count_zero >= 2:
            return [0] * len(nums)
        if count_zero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = temp
                else:
                    res[i] = 0
            return res
        if count_zero == 0:
            for i in range(len(nums)):
                res[i] = temp // nums[i]
            return res


        
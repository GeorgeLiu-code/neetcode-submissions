class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for num in nums:
            temp = 0
            curr = num
            while curr in nums_set:
                curr += 1
                temp += 1
            res = max(res,temp)
        return res
        
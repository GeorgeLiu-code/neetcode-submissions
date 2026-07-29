class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest  = 0
        nums_set = set(nums)
        for num in nums_set:
            curr = num
            temp = 0
            while curr in nums_set:
                curr += 1
                temp += 1
            longest = max(longest,temp)
        return longest 
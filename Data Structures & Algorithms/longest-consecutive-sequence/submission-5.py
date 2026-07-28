class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        nums_set = set(nums)
        longest = 0
        res = []
        if not nums:
            return 0
        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                while num+length in nums_set:
                    length += 1
                res.append(length)
        answer = max(res)
        return answer
            


        
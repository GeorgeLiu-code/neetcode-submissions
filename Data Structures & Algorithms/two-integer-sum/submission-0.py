class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                
                if nums[i]+nums[j] == target:
                    return [i,j]
        return None

        
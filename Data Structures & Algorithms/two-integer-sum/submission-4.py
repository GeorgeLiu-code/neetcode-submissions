class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,n in enumerate(nums):
            indices[n] = i
        for i,n in enumerate(nums): # {0:3, 1:4, 2:5, 3:6}
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i,indices[diff]]

        # if diff in indices. mean diff is a value can be consist of target.
        # so preserve diff's index indices[diff]. and why another index is i?
        # because when iterate value in indices. if another value is diff 
        # also in indices. must this two guys can consist of target.

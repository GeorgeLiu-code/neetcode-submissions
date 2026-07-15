class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        cost O(n), just need iterate one time then output the correct index.
        for loop iterate nums. using diff = target - nums[i] to record diff
        is in dictionary or not. if yes this iteration have the right element 
        can consist target. another value is in nums[i]. so return index 
        [diff's index, i] is [dictionary[diff], i].
        save nums index and value to dictionary. and we need return index.
        so save nums's index be dict value, nums's value be dict key. then
        find dict key just O(1) can find value.
        '''
        dictionary = {}
        for i,n in enumerate(nums):
            # will iterate  0:4, 1:5, 2:6
            diff = target - nums[i]
            if diff in dictionary:
                return [dictionary[diff],i]
            dictionary[n] = i
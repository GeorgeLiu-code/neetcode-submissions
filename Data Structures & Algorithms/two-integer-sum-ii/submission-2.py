class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in temp :
                return [temp[diff]+1, i+1]
            temp[n] = i
            

            
        
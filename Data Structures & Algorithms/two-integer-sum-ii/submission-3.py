class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            left,right = i+1,len(numbers)-1
            diff = target - n
            while left<=right:
                mid = left+(right-left)//2
                if numbers[mid] == diff:
                    return [i+1,mid+1]
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    right = mid -1
        return [] 

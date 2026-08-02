class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = []
        for i,n in enumerate(numbers):
            temp.append([n,i])
        left,right = 0, len(temp)-1
        while left < right:
            current = temp[left][0] + temp[right][0]
            if current == target:
                return [temp[left][1]+1,temp[right][1]+1]
            elif current < target:
                left += 1
            else :
                right -= 1
        
                   

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i,n in enumerate(nums):
            A.append([n,i])
        A.sort()
        # A = [[3,0],[4,1],[5,2],[6,3]]
        # using i and j be pointer visit all index
        i,j = 0, len(A)-1
        while i < j:
            current = A[i][0] + A[j][0] # value
            if current == target:
                return [min(A[i][1],A[j][1]),max([A[i][1],A[j][1]])] 
            elif current < target:
                i+=1
            else:
                j-=1




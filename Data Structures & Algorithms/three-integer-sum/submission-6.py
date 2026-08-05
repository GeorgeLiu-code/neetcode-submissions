class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1,len(nums)):
                count[nums[j]] -= 1
                if j> i + 1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])
            for j in range(i+1,len(nums)):
                count[nums[j]] += 1
        return res




        

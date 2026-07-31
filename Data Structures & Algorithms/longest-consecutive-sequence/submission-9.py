class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums=[2,20,4,10,3,4,5]
        temp = defaultdict(int)
        res = 0
        for num in nums:
            if temp[num] == 0:
            # if num not in temp:
                # use defaultdict will auto create key
                # so num usually in temp when use "if num not in temp:"
                # cause if not work
                temp[num] = temp[num-1] + temp[num+1] + 1
                temp[num - temp[num-1]] = temp[num]
                # if [5,6,7] length is 3 so T[5]=T[6]=T[7] = 3
                # now add 8 let T[8] = 4. then update total(two side) length
                # num = 8. 8- T[7] = 5 (key). so need update T[5] = 4 (length)
                
                temp[num + temp[num+1]] = temp[num]
                res = max(temp[num], res)
        return res


        
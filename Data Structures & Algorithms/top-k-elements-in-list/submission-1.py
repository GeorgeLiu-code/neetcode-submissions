class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3] , k = 2, output [2,3]

        count = defaultdict(int)
        for n in nums:
            count[n] += 1 # count is dict. key is number and value is frequent
          
            sortedn = sorted(count.items(), key = lambda item:item[1], reverse = True)
        # sorting count's value (frequent)

        result = []
        for num,freq in sortedn[0:k]: # get k number
            result.append(num)

        return result

            
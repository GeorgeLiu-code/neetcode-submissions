class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums=[1,2,2,3,3,3] k=2
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1 )]
        for i in range(len(nums)):
            count[nums[i]] += 1  # count key is number and value is frequent
        for num, time in count.items():
            freq[time].append(num) # freq = [[],[1],[2],[3],[],[],[]]
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]: # prevent put [] to res
                res.append(num)
                if len(res) == k:
                    return res


                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,3], k = 2
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1 # key is number, value is frequent
            # need use heap to sort frequent, to trans to arrray
        heap_array = []
        for num,frequent in count.items():
            heap_array.append([-frequent,num])
        
        heapq.heapify(heap_array) # use frequent heapify
        # heap_array = [[-3,3][-2,2][-1,1]]
        result = []
        for j in range(k):
            frequent, num = heapq.heappop(heap_array) # sort need heappop
            result.append(num)
        return result



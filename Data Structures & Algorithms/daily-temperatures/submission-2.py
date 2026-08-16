class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures=[30,38,30,36,35,40,28]

        n = len(temperatures)
        res = [0] * n
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:

                if res[j] == 0: # if next day is 0 then res[i] defalult 0
                                # need t[j] <= t[i] or all list 0
                    j = n       # pause j into next condition
                    break
                j += res[j]     # j+res[j]. then j-i is hotter interval
            if j < n:
                res[i] = j-i
        return res



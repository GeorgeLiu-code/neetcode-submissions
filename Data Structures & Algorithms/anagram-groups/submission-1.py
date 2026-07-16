class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # cost O(m*n). so need nested loop. and use tuple record their times
        # and let it be key. then append other similar value. finally return 
        # value.

        res = defaultdict(list)
        for word in strs:
            count = [0] * 26 # reset
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            res[tuple(count)].append(word) # key is tuple(count)
        return list(res.values())

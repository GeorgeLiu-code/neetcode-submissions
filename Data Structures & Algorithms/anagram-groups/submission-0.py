class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaultdict() and iterate strs. when iterate every word then
        # sort every word let it be key. then can append their similar value.
        # finally can return the list.
        
        res = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s)) # key
            res[sorteds].append(s)  # put similar word s in same key
        return list(res.values())




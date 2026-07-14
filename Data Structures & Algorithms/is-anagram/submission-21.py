class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char_s in s:
            count[char_s] = count.get(char_s,0) + 1
        for char_t in t:
            if char_t not in count:
                return False
            count[char_t] -=1
            if count[char_t] < 0:
                return False
        return True
                 

        
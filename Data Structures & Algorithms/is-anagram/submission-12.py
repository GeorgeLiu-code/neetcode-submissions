class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char_s in s:
            count[char_s] = count.get(char_s,0) + 1
            # key is char and value is times in diectionary
            if char_s not in t:
                return False
        for char_t in t:
            count[char_t] =count[char_t] - 1
            if count[char_t] < 0:
                return False
        return True

        
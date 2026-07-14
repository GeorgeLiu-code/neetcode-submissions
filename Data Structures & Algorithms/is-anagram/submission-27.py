class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26 # create a empty array, value all equal 0

        for i in range(len(s)):
            count[ord(s[i])-ord('a')] +=  1 # 'a' is baseline on index 0
            # initial value is 0. if s fit the alphabet then value increase 1
            count[ord(t[i])-ord('a')] -=  1
            # if t fit the alphabet then value decrease 1 

        for j in count:
            if j != 0:  # when count's value is not 0. s and t must different
                return False
        return True      
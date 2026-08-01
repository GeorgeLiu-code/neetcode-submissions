class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        con_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i].lower())
        con_str = "".join(arr)

        # temp_arr = []
        # temp_str = ""
        # for j in range(len(s)-1,-1,-1):
        #     if s[j].isalnum():
        #         temp_arr.append(s[j].lower())
        # temp_str = "".join(temp_arr)

        if con_str == con_str[::-1]:
            return True
        return False
                
        
        
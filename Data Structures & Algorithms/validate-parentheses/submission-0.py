class Solution:
    def isValid(self, s: str) -> bool:
        while ("{}" in s) or ("()" in s) or ("[]" in s): 
            s = s.replace("[]","") # just repalce closely parentheses
            s = s.replace("{}","") # so complexity N+(N-2)+(N-4)+...+2 = O(N^2)
            s = s.replace("()","")
        if s:
            return False
        return True
        
            

        

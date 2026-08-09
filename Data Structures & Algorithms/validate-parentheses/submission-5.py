class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {"(":")","{":"}","[":"]"}
        for n in s:
            if n in temp:
                stack.append(n)
            else: # n not in temp then n must be close
                if stack and temp[stack[-1]] == n:
                    stack.pop()
                else:
                    return False
        return not stack

        

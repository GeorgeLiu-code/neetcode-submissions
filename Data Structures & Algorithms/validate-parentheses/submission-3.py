class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {")":"(","]":"[","}":"{"}
        for n in s:
            if n not in temp:
                stack.append(n)
            else: # n in temp(key)
                if stack and temp[n] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

            
                

        
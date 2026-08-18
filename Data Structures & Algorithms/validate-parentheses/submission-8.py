class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {")":"(","}":"{","]":"[",}
        for n in s:
            if stack and n in temp:
                if temp[n] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else :
                stack.append(n)
        return not stack
        
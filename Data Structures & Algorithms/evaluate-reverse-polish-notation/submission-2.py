class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["2","1","+","3","*"]
        token=* right=3 left=+(be small root) recursion right=1 left=2
        1+2=3 back to 3*3=9
        """
        def DFS():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            right = DFS()
            left = DFS()
            if token == "+":
                return left + right
            if token == "-":
                return left - right
            if token == "*":
                return left * right
            if token == "/":
                return int(left / right)
        return DFS()
        
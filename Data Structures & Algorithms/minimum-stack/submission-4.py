class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            diff = val - self.mini
            self.stack.append(diff)
            if diff < 0:    # mean this val is more smaller
                self.mini = val

        # input [1,2,0]. stack will be [0,1,-1] then pop()
    def pop(self) -> None:
        diff = self.stack[-1]
        if diff < 0: # mini need fix
            self.mini = self.mini - diff
        self.stack.pop()

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.mini
        else:
            return diff + self.mini        

    def getMin(self) -> int:
        return self.mini
        

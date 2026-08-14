class Double:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = Double(tokens[0])
        curr = head
        for i in range(1,len(tokens)):
            curr.next = Double(tokens[i],prev=curr) # to find next node
            curr = curr.next # find this iteration curr
        while head is not None: # not head.val, because head may None first. then None.val will error
            if head.val in "+-*/":
                left = int(head.prev.prev.val)
                right = int(head.prev.val)
                if head.val == "+":
                    res = left + right
                elif head.val == "-":
                    res = left - right
                elif head.val == "*":
                    res = left * right
                else:
                    res = int(left / right)
                head.val = str(res)
                head.prev = head.prev.prev.prev # link previous node
                
                if head.prev is not None:
                    head.prev.next = head # link next node
            ans  = int(head.val) # must need or head.val = None
            head = head.next
        return ans


                


        
        

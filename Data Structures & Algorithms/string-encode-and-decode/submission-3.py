class Solution:
        # [] and [""] is different. can't just use .join()
        # because they all encode to "". so can't decode to original
        # ex. if strs = [] through .join(strs) will output "". 
        # then through .split(",") will output [""] but [] != [""]
        # .join return string. .splict return array

    def encode(self, strs: List[str]) -> str:
        s = ""
        for obj in strs:
            s += str(len(obj))
            s += "#"
            s += obj
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1  # j need to point "#"
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length # i need to point number
        return res
        

        

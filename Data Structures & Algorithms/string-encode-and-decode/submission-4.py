class Solution:

    def encode(self, strs: List[str]) -> str:
        # strs = ["Hello","World"]
        # encode = 5,5,#HelloWorld
        sizes = []
        res = []
        s= ""
        for obj in strs:
            sizes.append(str(len(obj))) # sizes = [5,5]
        for s in sizes:
            res.append(s)
            res.append(",")
        res.append("#")
        res.extend(strs)
        s = "".join(res)
        return s

    def decode(self, s: str) -> List[str]:
        # s = 5,5,#HelloWorld
        if not s:
            return []
        i = 0
        sizes = []
        res = []
        while s[i] != "#": # i need point number
            j= i
            while s[j] != ",": # j need point comma
                j += 1
            sizes.append(int(s[i:j])) 
            i = j+1
            # sizes  = [5,5]
        for length in sizes: # i = "#"
            res.append(s[i+1:i+1 + length])
            i = i+length

        return res





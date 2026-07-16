class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # list count have key letter and value times in the word
    # i need use count's value be res key
    # then res[key] will append word in same key
    # finally return res.values()
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1  
            res[tuple(count)].append(word)
        return list(res.values())

            
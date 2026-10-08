class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            res += word1[i]
            res += word2[i]

        if len(word1) == len(word2):
            return res
        
        elif len(word1) > len(word2):
            return res + word1[len(word2):len(word1)]

        else:   
            return res + word2[len(word1):len(word2)]

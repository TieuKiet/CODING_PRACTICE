class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        check = dict()
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in check:
                check[tuple(count)] = []
            check[tuple(count)].append(s)

        for value in check.values():
            res.append(value)
        return res
        
        


s = Solution()
print(s.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))
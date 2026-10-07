class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        n = 200
        min_str = strs[0]
        for s in strs:
            if len(s) < n:
                n = len(s)
                min_str = s

        is_substr = False
        for i in range(n):
            for s in strs:
                if s[i] != min_str[i]:
                    return res
                else:
                    is_substr = True
            res += s[i]



        return res


sol = Solution()
print(sol.longestCommonPrefix(["neet","feet"]))
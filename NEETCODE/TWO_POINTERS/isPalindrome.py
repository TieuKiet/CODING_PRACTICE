class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isascii() and c.isalnum() and c != " ":
                res += c.lower()

        return res == res[::-1]


s = Solution()
print(s.isPalindrome(s="Was it a car or a cat I saw?"))
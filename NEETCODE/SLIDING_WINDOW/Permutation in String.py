from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(len(s2) - n + 1):
            sub_str = s2[i:i+n]
            if Counter(sub_str) == Counter(s1):
                return True

        return False

s= Solution()
print(s.checkInclusion(s1 = "abc", s2 = "lecaabee"))
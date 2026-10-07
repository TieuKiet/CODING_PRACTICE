class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        check = [0 for _ in range(26)]

        for c in s:
            check[ord(c)- 97] += 1
            check_s = check
        check = [0 for _ in range(26)]

        for c in t:
            check[ord(c)- 97] += 1
            check_t = check
        
        
        print(check_t, check_s)
        for i in range(26):
            
            if check_s[i] != check_t[i]:
                return False        
        return True

s="racecar"
t="carrace"
sol = Solution()
ans = sol.isAnagram(s,t)
print(ans)
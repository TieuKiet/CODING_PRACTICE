class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        count = 1  
        if s == s[::-1]: return True
        while left < right:
            if s[left] != s[right]:
                if count == 0:
                    return False

                # remove left element
                remove_left = ""
                for i in range(len(s)):
                    if i != left:
                        remove_left += s[i]

                if remove_left == remove_left[::-1]:
                    return True
                    
                # remove right element
                remove_right = ""
                for i in range(len(s)):
                    if i != right:
                        remove_right += s[i]
                if remove_right == remove_right[::-1]:
                    return True
                count -= 1

            left += 1
            right -= 1
        
        return False
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        count = 1
        delete = ""
        is_valid = False
        if s == s[::-1]: return True
        while left < right:
            print(s[left],'|', s[right])
            if s[left] != s[right]:
                if count == 0:
                    return False
                # remove_left 
                remove_left = ""
                for i in range(len(s)):
                    if i != left:
                        remove_left += s[i]

                print(remove_left)
                if remove_left == remove_left[::-1]:
                    is_valid = True
                    

                remove_right = ""
                for i in range(len(s)):
                    if i != right:
                        remove_right += s[i]
                print(remove_right)
                if remove_right == remove_right[::-1]:
                    is_valid = True
                count -= 1

            left += 1
            right -= 1
        
        return is_valid




        
    
s = Solution()
print(s.validPalindrome(s="eedede"))
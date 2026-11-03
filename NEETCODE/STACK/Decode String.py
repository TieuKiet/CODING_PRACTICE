class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ""
        stack = []

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            
            elif c == '[':
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            
            elif c.isalpha():
                cur_str += c

            elif c == ']':
                prev_str, num = stack.pop()
                cur_str = prev_str + cur_str * num
        
        return cur_str




s = Solution()
print(s.decodeString(s = "2[a3[b]]c")) # output: "abbbabbbc"
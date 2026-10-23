class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            
            else:
                if stack == []:
                    return False

                t = stack.pop()
                if t == '(' and c != ')':
                    return False

                elif t == '[' and c != ']':
                    return False

                elif t == '{' and c != '}':
                    return False 
        
        if len(stack) != 0:
            return False
        return True

s = Solution()
print(s.isValid(s="["))
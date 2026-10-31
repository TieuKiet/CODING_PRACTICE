class Solution:
    def simplifyPath(self, path: str) -> str:
        res= ''
        stack = []
        arr= path.split('/')
        for c in arr:
            if c == '.' or c == '':
                continue

            elif c == '..':
                if not stack:
                    continue
                stack.pop()

            else:
                stack.append(c)

        for c in stack:
            res += '/'
            res+= c

        if res == '':
            return '/'
        return res
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = []
        for operation in operations:
            if operation != '+' and operation != 'C' and operation != 'D':
                res.append(int(operation))
            
            elif operation == '+':
                res.append(res[-1] + res[-2])
            
            elif operation == 'C':
                res.pop()
            
            elif operation == 'D':
                res.append(res[-1] * 2)

            print(res)
        
        return sum(res)

s = Solution()
print(s.calPoints(operations=["5","-2","4","C","D","9","+","+"]))

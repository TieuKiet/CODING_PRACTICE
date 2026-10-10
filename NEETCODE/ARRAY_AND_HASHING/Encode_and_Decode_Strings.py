class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            if len(s)<10:
                res += '00' +str(len(s))+ '#' + s

            elif len(s) < 100:
                res += '0' +str(len(s))+ '#' + s

            else:
                res += str(len(s))+ '#' + s
        
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 3
        while i < len(s):
            print(i,s[i])
            if s[i] == '#' and s[i-1].isdigit(): 
                
                n = int(s[i-3:i])
                res.append(s[i+1:i+n+1])
                i += 3 + n
            i += 1
        return res

s= Solution()

print(s.decode('001##007#5#hello014#12#longer text004#end#'))



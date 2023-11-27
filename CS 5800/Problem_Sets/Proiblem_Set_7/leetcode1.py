class Solution:
    def numDecodings(self, s: str) -> int:
        t=[0]*(len(s)+1)
        t[0]=1
        for i in range(1,len(s)+1):
            if s[i - 1] != '0':
                t[i] = t[i - 1]
            if i >= 2: 
                if 10 <= int(s[i - 2: i]) <= 26:
                    t[i] += t[i - 2]
        return t[i]
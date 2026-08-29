class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        b=0
        for char in s:
            if char=='(':
                a+=1
                b=max(b,a)
            elif char==')':
                a-=1
        return b            
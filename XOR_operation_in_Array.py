class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        final=0
        for i in range(0,n):
            opr=start + (2 * i)
            final ^= opr
        
        return final

    
Sol=Solution()
n=5
start=0
ans=Sol.xorOperation(n,start)
print(ans)
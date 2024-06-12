class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        ans=0
        for char in s:
            l.append(ord(char))
        for i in range(1,len(l)):
            ans += abs(l[i] - l[i-1])

        return ans
  
Sol=Solution()    
str="hello"
ans=Sol.scoreOfString(str)
print(ans)
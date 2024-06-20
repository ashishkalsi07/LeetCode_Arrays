class Solution(object):
    def findWordsContaining(self, words, x):
        ans=[]
        for index, word in enumerate(words):
            if x in word:
                ans.append(index)
        
        return ans


Sol=Solution()
words=["leet","code","abcde"]
x='e'
ans=Sol.findWordsContaining(words,x)
print(ans)
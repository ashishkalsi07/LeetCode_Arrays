class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count > max_words:
                max_words = word_count
        return max_words


S=Solution()
sent=["hi how are you","I am fine","okay","bye bye"]
ans=S.mostWordsFound(sent)
print(ans)
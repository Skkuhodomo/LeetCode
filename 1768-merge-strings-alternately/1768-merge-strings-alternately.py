class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)>len(word2):
            high=word1
        else:
            high=word2
        val=min(len(word1),len(word2))
        res1=high[val:]
        res=""
        i,j=0,0
        while i<len(word1) and j<len(word2):
            res+=word1[i]+word2[j]
            i+=1
            j+=1
        if len(word1) !=len(word2):
            return (res+res1)
        else:
            return (res)
                
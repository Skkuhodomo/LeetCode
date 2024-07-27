class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 더 긴 길이의 string을  high로 할당 
        if len(word1)>len(word2):
            high=word1
        else:
            high=word2
        val=min(len(word1),len(word2)) # 둘중 더 짧은 길이 찾기 
        cut_high=high[val:] # 긴 문자열을 더 짧은 길이 만큼 잘라주기 
        print(cut_high)
        res=""
        i,j=0,0
        while i<len(word1) and j<len(word2):
            res+=word1[i]+word2[j]
            i+=1
            j+=1
        if len(word1) !=len(word2):
            return (res+cut_high) 
        else:
            return (res)
                
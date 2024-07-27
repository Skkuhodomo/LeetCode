class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return KMP_search(needle, haystack)

def KMP_search(pat: str , txt:str ) -> int:
    pat_length = len(pat)
    txt_length = len(txt)
    lps = compute_LPS_array(pat)
    result = -1 
    i = 0 #txt에서의 인덱스
    j = 0 #pat에서의 인덱스 

    while i < txt_length :
        print('i:',i,'j:',j)
        if pat[j] == txt[i]: #일치하는 경우 인덱스를 1씩 증가 
            i += 1
            j += 1
        else: # 일치하지 않는 경우 lps array 정보를 이용하여 이동 
            if j != 0: 
                j = lps[j-1]
            else: 
                if j != 0:
                    j= lps[j-1]
                else: 
                    i+=1
        if j == pat_length: #패턴 하나 완벽히 찾음 
            result = i - j
            return result
        
    return result

def compute_LPS_array(pat:str) -> list:
    j = 0
    i = 1
    lps = [0]*len(pat)
    while i < len(pat) :
        if pat[i] == pat[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps
    

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        result =""
        # 정렬한 후, 양 끝을 찾습니다. 양 끝의 특징은 중간과 처음보다 더 멀겁니다. 
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]): #다르면 바로 끝
                return result 
            result +=first[i]
        return result  
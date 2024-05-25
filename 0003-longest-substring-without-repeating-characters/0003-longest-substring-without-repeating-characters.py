class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 해시맵을 통한 풀이. 새로 넣는 것이 존재하는 지 확인하는 전략.
        s_dic = {}
        result = 0 
        start = 0  # 슬라이딩 윈도우의 시작 위치
        
        for i, j in enumerate(s):
            # 이미 존재하는 경우, 시작 위치를 업데이트
            if j in s_dic and s_dic[j] >= start:
                start = s_dic[j] + 1
            
            s_dic[j] = i  # 현재 문자의 인덱스를 해시맵에 저장
            result = max(result, i - start + 1)  # 가장 긴 길이를 갱신
        
        return result
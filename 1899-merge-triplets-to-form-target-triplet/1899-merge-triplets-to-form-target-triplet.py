class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = set()  # 결과 판단을 위한 집합
        
        for t in triplets: 
            # 현재 삼중 배열 t가 target의 각 요소보다 큰지 확인
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                # t의 요소 중 하나라도 target의 대응하는 요소보다 크면 무시
                continue
            
            # t의 각 요소가 target의 대응 요소와 같은 경우 인덱스를 result 집합에 추가
            for i, v in enumerate(t):
                if v == target[i]:
                    result.add(i)
        
        # result에 0, 1, 2 세 개의 인덱스가 모두 존재하면 target을 만들 수 있음
        return len(result) == 3

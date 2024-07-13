class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        start,end = 0,0
        indexMap = defaultdict(int)
        # Greedy 알고리즘 활용 .
        for i,c in enumerate(s):
            indexMap[c]=i # 각 문자의 마지막 위치 저장 
        print(indexMap)
        for i,c in enumerate(s):
            end = max(end,indexMap[c]) # 처음엔 a의 끝인 8이 end로 변경. --> 8에 도달하면 조건문 돌며, 저장. 시작점은 9부터로 반복. 
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res
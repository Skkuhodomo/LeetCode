class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result  =  set() #결과 판단을 위한 집합 
        for t in triplets: 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: #타겟보다 각각 모두 큰 경우 
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    result.add(i)
        return len(result) == 3 
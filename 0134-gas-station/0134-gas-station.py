class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = []
        for i in range(len(gas)):
            arr.append(gas[i] - cost[i])
        print(arr)
        
        if sum(arr) < 0: 
            return -1 
        
        start = 0
        total = 0
        tank = 0
        
        for i in range(len(arr)):
            tank += arr[i]
            if tank < 0:
                # 현재까지의 합이 음수가 되는 경우
                # 다음 주유소를 시작점으로 설정
                start = i + 1
                # 누적된 값을 초기화
                tank = 0
        
        return start
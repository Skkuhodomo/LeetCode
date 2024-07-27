class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 나누어떨어지지 않으면, false
        if len(hand) % groupSize: 
            return False 
        # 해시맵 
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0) # 값이 없는 경우 0반환 
        # 해시맵의 키를 이용해 min_heap 
        min_heap = list(count.keys())
        heapq.heapify(min_heap) 

        # min_heap에서 pop을 하며, 해시맵의 value를 조정하며 조건 걸기
        while min_heap: 
            i = min_heap[0]
            for j in range(i, i+groupSize):
                if j not in count: #다음에 와야할 숫자가 count에 없을 때. 
                    return False 
                count[j] -= 1 # 있으면 하나 사용 
                if count[j] == 0:  # 사용하고 0개 남으면 
                    if j != min_heap[0]: # 그런게 그게 헤드가 아니면 false (다음에 연속이 되지 못하므로)
                        return False 
                    heapq.heappop(min_heap)
        return True


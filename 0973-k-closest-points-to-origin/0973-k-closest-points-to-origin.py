# Using heap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap) # O(n)
        # accessed O(1)
        # removed O(log n)
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap) # O(log n)
            res.append((x, y))
        return res
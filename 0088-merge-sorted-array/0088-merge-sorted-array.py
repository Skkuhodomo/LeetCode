import heapq as hq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        heap = []        
        for i in range(m):
            hq.heappush(heap, nums1[i])
        for i in range(n):
            hq.heappush(heap, nums2[i])
        for i in range(m + n):
            nums1[i] = hq.heappop(heap)
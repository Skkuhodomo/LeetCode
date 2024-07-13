import heapq as hq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        heap = []        
        for i in range(m):
            hq.heappush(heap, nums1[i])
        
        # Insert the elements of nums2 into the heap
        for i in range(n):
            hq.heappush(heap, nums2[i])
        
        # Extract elements from the heap and put them back into nums1
        for i in range(m + n):
            nums1[i] = hq.heappop(heap)
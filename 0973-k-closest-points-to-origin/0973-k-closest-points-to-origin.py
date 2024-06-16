# Using heap


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k개의 노드를 가진 최대 힙 생성
        maxHeap = []

        # 처음 k개의 점을 힙에 추가
        for x, y in points[:k]:
            dist = -(x ** 2 + y ** 2)  # 부호 반전하여 최대 힙처럼 동작하게 함
            maxHeap.append((dist, x, y))
        heapq.heapify(maxHeap)  # O(k)

        # 나머지 점들에 대해
        for x, y in points[k:]:
            dist = -(x ** 2 + y ** 2)
            # 새로운 점의 거리가 힙의 루트(가장 먼 점)보다 작은 경우
            if dist > maxHeap[0][0]:
                heapq.heapreplace(maxHeap, (dist, x, y))

        # 결과를 반환할 때 부호를 다시 반전하여 원래 거리로 돌려놓음
        return [[x, y] for (dist, x, y) in maxHeap]

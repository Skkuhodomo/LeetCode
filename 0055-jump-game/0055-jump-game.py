class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 마지막으로 도달할 수 있는 최대 인덱스를 기록
        max_reachable = 0
        
        for i, value in enumerate(nums):
            # 현재 인덱스가 이전까지의 최대 도달 인덱스를 넘는다면 불가능
            if i > max_reachable:
                return False
            # 현재 위치에서 도달할 수 있는 최대 인덱스를 갱신
            max_reachable = max(max_reachable, i + value)
        
        # 마지막 인덱스에 도달할 수 있으면 True 반환
        return max_reachable >= len(nums) - 1
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        result = 0
    
        while left < right:
            # 현재 left와 right 사이의 물의 양 계산
            current_area = (right - left) * min(height[left], height[right])
            result = max(result, current_area)
            
            # 높이가 더 낮은 쪽을 움직임.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sorting method
        # 절반 이상 --> 즉 중앙값이 최빈값이 됩니다. 
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
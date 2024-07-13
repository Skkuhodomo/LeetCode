class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sorting method
        # O(nlogn)
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
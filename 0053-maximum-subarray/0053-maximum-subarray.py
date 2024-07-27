#(Kadane's Algorithm)
class Solution:
    def maxSubArray(self, nums):
        cur_max, total_max = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            total_max = max(total_max, cur_max)
        return total_max
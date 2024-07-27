#(Kadane's Algorithm)
'''
첫 인덱스에서 시작해서 하나씩 가며, 처음이 음수가 아니도록 쭉 훑고 지나감
'''
class Solution:
    def maxSubArray(self, nums):
        cur_max, total_max = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            total_max = max(total_max, cur_max)
        return total_max


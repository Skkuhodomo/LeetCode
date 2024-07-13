class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mean = sum(nums)/len(nums)
        print(mean)
        ns = list(set(nums))
        distance = ((mean-ns[0]))**2
        m = 0
        for i in range(len(ns)):
            if distance >= (mean-ns[i])**2:
                m = ns[i]
                distance >= (mean-ns[i])**2
                

        return m
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        sum_list = nums1 + nums2
        sum_list.sort()
        print(sum_list)
        #odd or even 
        #짝
        if len(sum_list) % 2 == 0:
            m = len(sum_list) // 2
            return (sum_list[(m)] + sum_list[(m-1)])/2
        #홀
        else: 
            m = (len(sum_list)-1) // 2
            return sum_list[m]/1

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # nums1이 더 작은 배열이 되도록 보장합니다.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # i가 너무 작을 때, 증가시킵니다.
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            # i가 너무 클 때, 감소시킵니다.
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # i가 적절할 때
                if i == 0: 
                    max_of_left = nums2[j - 1]
                elif j == 0: 
                    max_of_left = nums1[i - 1]
                else: 
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                # 배열의 총 길이가 홀수인 경우, 중앙값은 max_of_left 입니다.
                if (m + n) % 2 == 1:
                    return max_of_left

                # 배열의 총 길이가 짝수인 경우, 중앙값은 max_of_left와 min_of_right의 평균입니다.
                if i == m: 
                    min_of_right = nums2[j]
                elif j == n: 
                    min_of_right = nums1[i]
                else: 
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0



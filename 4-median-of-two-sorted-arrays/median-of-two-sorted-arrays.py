class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        new_list = [0] * (m + n)
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                new_list[k] = nums1[i]
                k += 1
                i += 1
            else:
                new_list[k] = nums2[j]
                k += 1
                j += 1
        while i < m:
            new_list[k] = nums1[i]
            k += 1
            i += 1
        while j < n:
            new_list[k] = nums2[j]
            k += 1
            j += 1
        p = m + n
        if p % 2 == 0:
            ans = (new_list[p // 2 - 1] + new_list[p // 2]) / 2
        else:
            ans = new_list[p // 2]
        return ans
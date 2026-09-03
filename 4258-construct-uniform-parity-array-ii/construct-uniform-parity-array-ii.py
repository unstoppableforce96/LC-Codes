class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        if mn % 2 == 1:
            return True
        else:
            are_all_even = True
            for i in nums1:
                if i % 2 == 1:
                    are_all_even = False
                    break
            return are_all_even
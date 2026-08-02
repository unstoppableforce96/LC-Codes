class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        ans = 0
        original = a / b
        
        for start in range(n):
            e_count = o_count = 0
            for end in range(start, n):
                if nums[end] % 2 == 0:
                    e_count += 1
                else:
                    o_count += 1
                if o_count > 0 and e_count / o_count <= original:
                    ans += 1
        return ans
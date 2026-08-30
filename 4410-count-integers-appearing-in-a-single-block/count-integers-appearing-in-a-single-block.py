class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        ans = 0
        for k, v in d.items():
            is_single_block = True
            for j in range(1, len(v)):
                if v[j] - v[j - 1] > 1:
                    is_single_block = False
                    break
            if is_single_block:
                ans += 1
        return ans
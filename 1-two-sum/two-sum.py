class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d.keys():
                return [i, d[diff]]
            else:
                d[nums[i]] = i
        return [-1, -1]

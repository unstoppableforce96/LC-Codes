class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        rs = 0
        for i in nums:
            rs += i
            prefix_sum.append(rs)
        return prefix_sum
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Case-1: Largest - 3rd smallest
        val1 = nums[-1] - nums[2]

        #Case-2: 3rd Largest - Smallest
        val2 = nums[-3] - nums[0]

        #Case-3: 2nd Largest - 2nd Smallest
        val3 = nums[-2] - nums[1]

        return min(val1, val2, val3)
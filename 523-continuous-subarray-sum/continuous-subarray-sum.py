class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1} # storing the index
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            req = prefix % k
            if req in seen:
                dist = i - seen[req]
                if dist >= 2:
                    return True
            if prefix%k not in seen:
                seen[prefix%k] = i
        return False
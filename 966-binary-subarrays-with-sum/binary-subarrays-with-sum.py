class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0: 1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            req = prefix - goal
            if req in seen:
                ans += seen[req]
            
            seen[prefix] = seen.get(prefix, 0) + 1
        return ans
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        ans = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]

            req = prefix - k
            if req in seen:
                ans += seen[req]
            seen[prefix] = seen.get(prefix, 0) + 1
        return ans

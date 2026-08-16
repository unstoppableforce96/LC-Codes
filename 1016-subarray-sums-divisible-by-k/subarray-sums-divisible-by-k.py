class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        subCount = 0
        prefixSum = 0
        for i in nums:
            prefixSum += i
            req = prefixSum % k
            if req in seen:
                subCount += seen[req]
            seen[prefixSum % k] = seen.get(prefixSum % k, 0) + 1
        return subCount

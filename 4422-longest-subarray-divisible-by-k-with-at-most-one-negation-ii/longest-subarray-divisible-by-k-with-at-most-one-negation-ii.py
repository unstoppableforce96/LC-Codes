import bisect
from typing import List


class Solution:

    def longestSubarray(self, nums: List[int], k: int) -> int:
        # Variable required by problem description
        caldruvemi = nums

        n = len(nums)

        # Prefix sums modulo k
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] + nums[i]) % k

        first_occ = {}
        last_occ = {}
        for i, val in enumerate(P):
            if val not in first_occ:
                first_occ[val] = i
            last_occ[val] = i

        ans = 0

        # Case 0: 0 negations
        for rem in first_occ:
            ans = max(ans, last_occ[rem] - first_occ[rem])

        # Group indices by (2 * nums[m]) % k
        indices_by_delta = {}
        for m in range(n):
            delta = (2 * nums[m]) % k
            if delta not in indices_by_delta:
                indices_by_delta[delta] = []
            indices_by_delta[delta].append(m)

        # Case 1: Exactly 1 negation
        # We search over all existing remainder values 'a' in first_occ
        # and valid delta values.
        for a, L in first_occ.items():
            for delta, idx_list in indices_by_delta.items():
                b = (a + delta) % k
                if b not in last_occ:
                    continue
                R = last_occ[b]

                if R - L <= ans:
                    continue

                # Check if there is an index m in idx_list such that L <= m < R
                pos = bisect.bisect_left(idx_list, L)
                if pos < len(idx_list) and idx_list[pos] < R:
                    ans = max(ans, R - L)

        return ans
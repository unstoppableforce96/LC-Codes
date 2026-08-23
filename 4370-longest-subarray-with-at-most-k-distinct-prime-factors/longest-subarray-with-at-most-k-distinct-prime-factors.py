def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def get_primes(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                s.add(i)
            if is_prime(n // i):
                s.add(n//i)
    return s
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        left = 0
        prime_factors = []
        longest = 0
        d = {}
        pf = {}
        for right in range(len(nums)):
            s = get_primes(nums[right])
            for i in s:
                pf[i] = pf.get(i, 0) + 1
            d[nums[right]] = s
            # print(nums[right], s, d, prime_factors)
            while len(pf) > k:
                remove = nums[left]
                for j in d[remove]:
                    pf[j] -= 1
                    if pf[j] == 0:
                        pf.pop(j)
                left += 1
            longest = max(longest, right - left + 1)
        return longest


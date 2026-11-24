def get_gcd(a, b):
    while a and b:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a if a else b
    
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for start in range(n):
            for end in range(start, n):
                prod = 1
                for i in range(start, end + 1):
                    prod *= nums[i]
                if prod == lcm(*nums[start: end + 1]) * gcd(*nums[start: end + 1]):
                    ans = max(ans, end - start + 1)
        return ans
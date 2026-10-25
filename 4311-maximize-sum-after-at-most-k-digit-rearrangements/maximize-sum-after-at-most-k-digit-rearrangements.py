def get_max(n):
    lst = list(str(n))
    lst.sort(reverse=True)
    return int(''.join(lst))
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        ans = 0
        diff = []
        for i in nums:
            diff.append(get_max(i) - i)
        ans = sum(nums)
        diff.sort(reverse=True)
        for i in range(k):
            ans += diff[i]
        return ans
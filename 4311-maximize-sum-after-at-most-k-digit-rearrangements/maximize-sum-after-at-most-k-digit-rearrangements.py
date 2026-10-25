def get_max(n):
    lst = list(str(n))
    lst.sort(reverse=True)
    return int(''.join(lst))
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        new = []
        ans = 0
        for i in nums:
            inner = [i, get_max(i)]
            inner.sort(reverse=True)
            new.append(inner)
        new.sort(reverse=True)
        diff = []
        for i in new:
            diff.append(i[0] - i[1])
        ans = sum(nums)
        diff.sort(reverse=True)
        for i in range(k):
            ans += diff[i]
        return ans
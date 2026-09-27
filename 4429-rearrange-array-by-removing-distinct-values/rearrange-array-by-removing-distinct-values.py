class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        f = [0] * 101
        for i in nums:
            f[i] += 1
        d = deque()
        for i in range(len(f)):
            if f[i] > 0:
                d.append(i)
        ans = []
        while d:
            if f[d[0]] > 0:
                ans.append(d[0])
                f[d[0]] -= 1
            if f[d[0]] > 0:
                d.append(d.popleft())
            else:
                d.popleft()
        return ans
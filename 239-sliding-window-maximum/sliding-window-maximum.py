class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        d.append(0)
        ans = []
        for i in range(1, k):
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)
        ans.append(nums[d[0]])
        for i in range(k, len(nums)):
            # and element (i - k) will always expire
            # just remove it from deque if it's present
            if d[0] == i - k:
                d.popleft()
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            d.append(i)
            ans.append(nums[d[0]])
        return ans
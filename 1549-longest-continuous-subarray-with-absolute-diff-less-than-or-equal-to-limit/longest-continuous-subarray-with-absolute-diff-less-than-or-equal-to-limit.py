class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        ans = 0
        left = 0
        for i in range(len(nums)):
            # updating max deque
            while max_dq and nums[i] > nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(i)

            # updating min deque
            while min_dq and nums[i] < nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(i)

            # window validation
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                
                left += 1
            ans = max(ans, i - left + 1)
        return ans
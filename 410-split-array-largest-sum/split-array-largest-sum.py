def feasible(nums, k, guess_sum):
    needed_k = 0
    current_sum = 0
    for i in range(len(nums)):
        if current_sum + nums[i] > guess_sum:
            needed_k += 1
            current_sum = nums[i]
        else:
            current_sum += nums[i]
    if current_sum != 0:
        needed_k += 1
    return needed_k <= k
        
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            if feasible(nums, k, mid):
                high = mid
            else:
                low = mid + 1
        return low
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        odds = 0
        subs_with_c_right = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1
                subs_with_c_right = 0
            while odds == k:
                if nums[left] % 2 == 1:
                    odds -= 1     
                subs_with_c_right += 1
                left += 1
            ans += subs_with_c_right
        return ans
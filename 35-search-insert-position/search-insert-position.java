class Solution 
{
    public int searchInsert(int[] nums, int target) 
    {
        int len = nums.length , left = 0 , right = len-1 , mid = 0;

        while(left <= right)
        {
            mid = (right+left)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                left = mid+1;
            else 
                right = mid-1;
        }
        if(nums[mid] < target)
            return mid+1;
        return mid;
    }
}
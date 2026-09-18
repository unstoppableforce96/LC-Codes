class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int numsSize1 = nums1.size();
        vector<int> res;
        int numSize2 = nums2.size();
        for(int i = 0; i < numsSize1; i++)
        {
            bool found = false;
            bool push = false;
            for (int j = 0; j < numSize2; j++)
            {
                if(nums1[i]==nums2[j])
                found = true;
                if(found && nums2[j] > nums1[i])
                {
                    res.push_back(nums2[j]);
                    push = true;
                    break;
                }
            }
            if(!push)
            res.push_back(-1);
        }
        return res;
    }
};
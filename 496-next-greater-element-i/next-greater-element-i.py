class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}
        for i in nums2:
            while st and i > st[-1]:
                d[st[-1]] = i
                st.pop()
            st.append(i)
        for i in st:
            d[i] = -1
        ans = []
        for k in nums1:
            ans.append(d[k])
        return ans
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse1 = [n] * n
        st = []
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                popped = st.pop()
                nse1[popped] = i
            st.append(i)
        
        nse2 = [-1] * n
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and heights[i] < heights[st[-1]]:
                popped = st.pop()
                nse2[popped] = i
            st.append(i)
        
        max_area = 0
        for i in range(n):
            height = heights[i]
            width = nse1[i] - nse2[i] - 1
            area = height * width
            max_area = max(area, max_area)
        return max_area
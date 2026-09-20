class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        nse = [n] * n
        pse = [-1] * n
        st = []
        for i in range(len(heights)):
            while st and heights[i] < heights[st[-1]]:
                nse[st.pop()] = i
            st.append(i)
        st.clear()
        for i in range(len(heights) - 1, -1, -1):
            while st and heights[i] < heights[st[-1]]:
                pse[st.pop()] = i
            st.append(i)
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            height = heights[i]
            area = width * height
            max_area = max(area, max_area)
        return max_area


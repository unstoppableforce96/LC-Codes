class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        max_area = 0
        for i in range(n + 1):
            current_height = 0 if i == n else heights[i]
            while st and current_height < heights[st[-1]]:

                # found NSE -> heights[i] is the NSE of st[-1]
                right_smaller = i  

                # pop st top
                bar = st.pop()

                # Now whatever the element is on stack top is the Left smaller
                if st:
                    left_smaller = st[-1]
                else:
                    left_smaller = -1
                
                # Calculate area
                area = (right_smaller - left_smaller - 1) * heights[bar]
                max_area = max(area, max_area)
            st.append(i)
        print(st)
        return max_area

                
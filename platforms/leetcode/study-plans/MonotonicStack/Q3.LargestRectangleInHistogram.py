class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] 
        max_area = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h_idx = stack.pop()
                h = heights[h_idx]

                left_smaller_idx = stack[-1] if stack else -1
                width = i - left_smaller_idx - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        while stack:
            h_idx = stack.pop()
            h = heights[h_idx]
            left_smaller_idx = stack[-1] if stack else -1
            width = n - left_smaller_idx - 1
            max_area = max(max_area, h * width)

        return max_area

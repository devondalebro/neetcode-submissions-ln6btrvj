class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for each bar, we find the bars till a lower bar (on the right)
        right_bound = [0] * len(heights)
        for i in range(len(heights)):
            right_bound[i] = len(heights) - i
        inc_stack = []
        for i, h in enumerate(heights):
            while len(inc_stack) and h < inc_stack[-1][1]:
                right_bound[inc_stack[-1][0]] = i - inc_stack[-1][0]
                inc_stack.pop()
            inc_stack.append((i, h))

        # for each bar, we find the bars till a lower bar (on the left)
        heights.reverse()
        left_bound = [0] * len(heights)
        for i in range(len(heights)):
            left_bound[i] = len(heights) - i
        inc_stack = []
        for i, h in enumerate(heights):
            while len(inc_stack) and h < inc_stack[-1][1]:
                left_bound[inc_stack[-1][0]] = i - inc_stack[-1][0]
                inc_stack.pop()
            inc_stack.append((i, h))
        left_bound.reverse()    
        print(left_bound)
        print(right_bound)
        heights.reverse()
        
        # we now compute the largest area
        max_area = 0
        for i, h in enumerate(heights):
            max_area = max(h * (left_bound[i] + right_bound[i] - 1), max_area)
            
        return max_area

class Solution:
    from typing import List 
    def maxArea(self, numbers: List[int]) -> int:
        left, right, max_res = 0, len(numbers) - 1, 0
        while left < right:
            res = min(numbers[left], numbers[right]) * (right - left)
            if numbers[left] < numbers[right]:
                left += 1
            else: 
                right -= 1
            if res > max_res:
                max_res = res 
        return max_res

# Runtime 63 ms, 94.06 %
# Memory 28.56 mb, 13.97 %
def main():
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(numbers=height))

if __name__ == '__main__':
    main()
